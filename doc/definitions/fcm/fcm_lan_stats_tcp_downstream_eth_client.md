# Testcase fcm_lan_stats_tcp_downstream_eth_client

## Environment setup and dependencies

Ensure DUT is in OpenSync default state, as is after boot.\
Wireless client must be connected to the DUT.\
Ethernet client must be connected to the leaf pod. \
DUT has WAN connectivity.\
MQTT daemon is running on RPI server.

## Testcase description

The goal of this testcase is to verify:

- LAN stats are generated for downstream TCP traffic from WiFi client connected
  to the GW to the Ethernet client connected to the leaf pod.

## Expected outcome and pass criteria

After:

- Client device is successfully connected to the DUT.
- Egress and ingress rules are configured in the `Openflow_Config` table.
- `FCM_Collector_Config`, `AWLAN_Node`, `FCM_Report_Config`, `FCM_Filter` and
  `Openflow_Tag` tables are configured.
- Downstream TCP traffic is generated from the WiFi client using `iperf`.

MQTT report should contain LAN stats for the downstream TCP flow.

## Implementation status

Not Implemented
