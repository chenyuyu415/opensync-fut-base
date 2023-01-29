test_inputs = {
    "brv_busybox_builtins": {
        'args_mapping': [
            "busybox_builtin",
        ],
        'inputs': [
            "[",
            "[[",
            "arping",
            "ash",
            "awk",
            "base64",
            "basename",
            "cat",
            "chmod",
            "cmp",
            "cp",
            "cut",
            "date",
            "dd",
            "devmem",
            "df",
            "dirname",
            "dmesg",
            "du",
            "echo",
            "egrep",
            "env",
            "expr",
            "false",
            "find",
            "free",
            "grep",
            "gunzip",
            "gzip",
            "halt",
            "head",
            "hexdump",
            "kill",
            "killall",
            "ln",
            "logger",
            "ls",
            "lspci",
            "md5sum",
            "mkdir",
            "mkfifo",
            "mknod",
            "mktemp",
            "mount",
            "mv",
            "nc",
            "netstat",
            "nslookup",
            "passwd",
            "pgrep",
            "pidof",
            "pivot_root",
            "printf",
            "ps",
            "pwd",
            "readlink",
            "reboot",
            "rm",
            "rmdir",
            "route",
            "sed",
            "seq",
            "sh",
            "sleep",
            "sort",
            "start-stop-daemon",
            "strings",
            "sync",
            "tail",
            "tar",
            "tee",
            "test",
            "timeout",
            "touch",
            "tr",
            "true",
            "udhcpc",
            "umount",
            "uname",
            "uptime",
            "vconfig",
            "vi",
            "wc",
            "wget",
            "which",
            "xargs",
            "yes",
            "zcat",
        ],
    },
    "brv_is_script_on_system_fut": {
        'args_mapping': [
            "system_script",
        ],
        "inputs": [
            "/etc/init.d/healthcheck",
            "/etc/init.d/manager",
            "/etc/init.d/openvswitch",
            "/proc/net/vlan/config",
            "/sbin/udhcpc",
            "/tmp/resolv.conf",
            "/usr/opensync/etc/kconfig",
            "/var/etc/dnsmasq.conf",
            "/usr/opensync/bin/wpd",
        ],
    },
    "brv_is_tool_on_system_fut": {
        'args_mapping': [
            "system_tool",
        ],
        'inputs': [
            "[",
            "[[",
            "awk",
            "basename",
            "break",
            "case",
            "cat",
            "cd",
            "chmod",
            "curl",
            "cut",
            "date",
            "do",
            "echo",
            "eval",
            "exit",
            "export",
            "false",
            "find",
            "for",
            "getopts",
            "grep",
            "head",
            "hostapd",
            "hostapd_cli",
            "if",
            "ifconfig",
            "ip",
            "iptables",
            "kill",
            "killall",
            "ls",
            "miniupnpd",
            "mkdir",
            "ovs-ofctl",
            "ovs-vsctl",
            "ovs-vswitchd",
            "ovsdb-server",
            "ovsh",
            "pgrep",
            "pidof",
            "ping",
            "ping6",
            "printf",
            "ps",
            "return",
            "rm",
            "route",
            "scp",
            "sed",
            "seq",
            "set",
            "sh",
            "shift",
            "sleep",
            "source",
            "ssh",
            "tail",
            "tar",
            "test",
            "touch",
            "tr",
            "trap",
            "true",
            "type",
            "udhcpc",
            "wc",
            "which",
            "while",
            "wpa_cli",
            "wpa_supplicant",
        ],
    },
    "brv_is_tool_on_system_opensync": {
        'args_mapping': [
            "system_tool",
        ],
        'inputs': [
            "ash",
            "base64",
            "brctl",
            "cp",
            "dd",
            "devmem",
            "df",
            "dirname",
            "dnsmasq",
            "du",
            "egrep",
            "env",
            "expr",
            "free",
            "hexdump",
            "hostapd_cli",
            "ifdown",
            "ifup",
            "ip6tables-restore",
            "iptables-restore",
            "less",
            "logger",
            "lspci",
            "md5sum",
            "mkfifo",
            "mknod",
            "mktemp",
            "odhcp6c",
            "ovs-appctl",
            "ovs-dpctl",
            "passwd",
            "pivot_root",
            "pppd",
            "pwd",
            "read",
            "reboot",
            "rmdir",
            "scp",
            "sort",
            "start-stop-daemon",
            "strings",
            "tcpdump",
            "tee",
            "timeout",
            "umount",
            "uname",
            "uptime",
            "vconfig",
            "vi",
            "wpa_cli",
            "wpa_supplicant",
            "xargs",
            "yes",
            "zcat",
        ],
    },
    "brv_ovs_check_version": {},
}