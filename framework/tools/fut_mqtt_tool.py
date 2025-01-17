#!/usr/bin/env python3

"""Module to create an MQTT client, establish a connection to the MQTT broker, subscribe to a topic and collect messages."""

import argparse
import signal
import sys
from statistics import mean

from framework.tools.functions import output_to_json
from lib_testbed.generic.mqtt.mqtt_client import MqttClient
from lib_testbed.generic.mqtt.opensync_stats_pb2 import Report as StatsReportSchema


def parse_arguments():
    """Standalone method to parse script input arguments."""
    parser = argparse.ArgumentParser(
        description='Initiate MQTT connection and subscribe to topic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        '--hostname',
        type=str,
        required=True,
        help='MQTT server hostname',
    )
    parser.add_argument(
        '--port',
        type=int,
        required=True,
        help='Port to connect to',
    )
    parser.add_argument(
        '--topic',
        type=str,
        required=True,
        help='Topic to subscribe to',
    )
    parser.add_argument(
        '--ca_cert',
        type=str,
        required=True,
        help='Path to CA certificate file',
    )
    parser.add_argument(
        '--max_message_count',
        type=int,
        required=False,
        default=1,
        help='Number of new messages to wait for',
    )
    parser.add_argument(
        '--timeout',
        type=int,
        required=False,
        default=300,
        help='Time to wait for new messages',
    )
    parser.add_argument(
        '--collect_messages',
        type=bool,
        required=False,
        help='Collect a specified number of messages, disconnect after collection is completed',
    )
    parser.add_argument(
        '--stdout_output',
        type=bool,
        required=False,
        help='Write the collected messages to standard output',
    )
    parser.add_argument(
        '--json_output',
        type=bool,
        required=False,
        help='Write the collected messages to a JSON file',
    )
    input_args = parser.parse_args()
    return input_args


def extract_mqtt_data(data, value_list, data_key, simplify=False):
    """Extract data from the collected MQTT messages.

    Args:
        data (dict): Data in a dictionary format
        value_list (list): Empty list used to store extracted data
        data_key (str): Define the key for which the values are extracted
        simplify (bool): If element is a list of type int the average value is calculated,
                         if element is a list of type str or bool only the first element
                         is returned if all elements are equal
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if data_key in data.keys():
                value_list.append(data[data_key])
                break
            if isinstance(value, (dict, list)):
                if key == data_key:
                    value_list.append(value)
                else:
                    extract_mqtt_data(value, value_list, data_key)
            elif key == data_key:
                value_list.append(value)
    elif isinstance(data, list):
        for item in data:
            extract_mqtt_data(item, value_list, data_key)
    if simplify:
        for element in value_list:
            if isinstance(element, (str, bool)):
                if all(element == value_list[0] for element in value_list):
                    value_list = value_list[0]
                    break
            elif isinstance(element, (int, float)):
                value_list = round(mean(value_list), 4)
                break
    return value_list


def extract_mqtt_data_as_dict(data, data_keys, simplify=False):
    """Extract multiple values from the collected MQTT messages and output them in a dictionary format.

    Args:
        data (dict): Data in a dictionary format
        data_keys (list): Define the list of keys for which the values are extracted
        simplify (bool): Simplify the extracted data
    """
    extracted_data = []
    for data_key in data_keys:
        value_list = []
        extracted_data.append(extract_mqtt_data(data, value_list, data_key, simplify))
        if not value_list:
            raise Exception(f'Failed to extract data from the MQTT messages for the following key: {data_key}')
    extracted_data_dict = dict(zip(data_keys, extracted_data))
    return extracted_data_dict


def signal_handler(sig, frame):
    """Handle the signal.

    Args:
        sig (_type_): Not used
        frame (_type_): Not used
    """
    sys.exit(0)


if __name__ == '__main__':
    # Accept Ctrl+C as a signal interrupt
    signal.signal(signal.SIGINT, signal_handler)

    # Parse input arguments
    input_args = parse_arguments()
    hostname = input_args.hostname
    port = input_args.port
    topic = input_args.topic
    ca_cert = input_args.ca_cert
    max_message_count = input_args.max_message_count
    timeout = input_args.timeout
    collect_messages = input_args.collect_messages
    stdout_output = input_args.stdout_output
    json_output = input_args.json_output

    # Derived arguments
    mqtt_config = {
        "mqtt_hostname": [hostname],
        "mqtt_port": port,
        "certs": {
            "ca_cert": ca_cert,
        },
    }

    mqtt_client = MqttClient(mqtt_config)
    # Change StatsReportSchema() if the usage of a different protobuf decoder is required
    mqtt_client.report_proto = StatsReportSchema()
    mqtt_client.connect(mqtt_config['mqtt_hostname'], topic, certs=mqtt_config['certs'])

    if collect_messages:
        mqtt_client.wait_messages(timeout, new_messages_count=max_message_count)

    if stdout_output:
        # Write the collected messages to standard output
        for message in mqtt_client.messages:
            sys.stdout.write(f'{message}')

    if json_output:
        # Create JSON file and populate it with the collected MQTT messages
        output_to_json(mqtt_client.messages, '/tmp/mqtt_messages.json', sort_keys=False)
