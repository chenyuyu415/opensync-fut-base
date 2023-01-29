test_cfg = {
    "othr_add_client_freeze": [
        {
            "channel": 6,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 11,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 36,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 48,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 149,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
        {
            "channel": 157,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
    ],
    "othr_connect_wifi_client_multi_psk": [
        {
            "channel": 6,
            "ht_mode": "HT40",
            "psk_a": "multi_psk_a",
            "psk_b": "multi_psk_b",
            "radio_band": "24g",
        },
        {
            "channel": 11,
            "ht_mode": "HT40",
            "psk_a": "multi_psk_a",
            "psk_b": "multi_psk_b",
            "radio_band": "24g",
        },
        {
            "channel": 36,
            "ht_mode": "HT40",
            "psk_a": "multi_psk_a",
            "psk_b": "multi_psk_b",
            "radio_band": "5gl",
        },
        {
            "channel": 48,
            "ht_mode": "HT40",
            "psk_a": "multi_psk_a",
            "psk_b": "multi_psk_b",
            "radio_band": "5gl",
        },
        {
            "channel": 149,
            "ht_mode": "HT40",
            "psk_a": "multi_psk_a",
            "psk_b": "multi_psk_b",
            "radio_band": "5gu",
        },
        {
            "channel": 157,
            "ht_mode": "HT40",
            "psk_a": "multi_psk_a",
            "psk_b": "multi_psk_b",
            "radio_band": "5gu",
        },
    ],
    "othr_connect_wifi_client_to_ap": [
        {
            "channel": 6,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 11,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 36,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 48,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 149,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
        {
            "channel": 157,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
    ],
    "othr_verify_eth_lan_iface_wifi_master_state": [
        {},
    ],
    "othr_verify_eth_wan_iface_wifi_master_state": [
        {},
    ],
    "othr_verify_ethernet_backhaul": [
        {
            "ignore_collect": True,
            "ignore_collect_msg": "FAIL: FUT location file fix required",
        },
    ],
    "othr_verify_gre_iface_wifi_master_state": [
        {
            "channel": 6,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 11,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 36,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 48,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 149,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
        {
            "channel": 157,
            "ht_mode": "HT20",
            "radio_band": "5gu",
        },
    ],
    "othr_verify_gre_tunnel_dut_gw": [
        {
            "channel": 6,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 11,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 36,
            "encryption": "WPA2",
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 48,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 149,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
        {
            "channel": 157,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
        {
            "channel": 6,
            "encryption": "WPA3",
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 36,
            "encryption": "WPA3",
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 48,
            "encryption": "WPA3",
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 149,
            "encryption": "WPA3",
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
        {
            "channel": 157,
            "encryption": "WPA3",
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
    ],
    "othr_verify_iperf3_speedtest": [
        {
            "traffic_type": "forward",
        },
        {
            "traffic_type": "reverse",
        },
        {
            "traffic_type": "udp",
        },
    ],
    "othr_verify_lan_bridge_iface_wifi_master_state": [
        {},
    ],
    "othr_verify_ookla_speedtest": [
        {
            "ignore_collect": True,
            "ignore_collect_msg": "FAIL: ookla binary does not exist on system",
        },
    ],
    "othr_verify_ookla_speedtest_bind_options": [
        {
            "ignore_collect": True,
            "ignore_collect_msg": "FAIL: ookla binary does not exist on system",
        },
    ],
    "othr_verify_ookla_speedtest_bind_reporting": [
        {
            "ignore_collect": True,
            "ignore_collect_msg": "FAIL: ookla binary does not exist on system",
        },
    ],
    "othr_verify_ookla_speedtest_sdn_endpoint_config": [
        {
            "speedtest_config_path": "http://config.speedtest.net/v1/embed/x340jwcv4nz2ou3r/config",
        },
    ],
    "othr_verify_samknows_process": [
        {},
    ],
    "othr_verify_vif_iface_wifi_master_state": [
        {},
    ],
    "othr_verify_wan_bridge_iface_wifi_master_state": [
        {
            "ignore_collect": True,
            "ignore_collect_msg": "NOT_APPLICABLE: Testcase not applicable to WANO enabled devices",
        },
    ],
    "othr_wifi_disabled_after_removing_ap": [
        {
            "channel": 6,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 11,
            "ht_mode": "HT40",
            "radio_band": "24g",
        },
        {
            "channel": 36,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 48,
            "ht_mode": "HT40",
            "radio_band": "5gl",
        },
        {
            "channel": 149,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
        {
            "channel": 157,
            "ht_mode": "HT40",
            "radio_band": "5gu",
        },
    ],
}