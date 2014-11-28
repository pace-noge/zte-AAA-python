
class BaseCommand:

    def config_terminal(self):
        return ["config terminal"]

    def select_interface(self, interface):
        """
        olt interface:
        interface = gpon-olt_1/2/2
        onu interface:
        interface = gpon-onu_1/2/2:1
        """
        return ["interface %s" % interface]

    def set_onu_info(self, onunum, type="ZTEG-F660", sn):
        """
        onunum: onu number inside olt
        type: ZTEG-F660
        """
        return ["onu %s type %s sn %s" % (self.onunum, self.type, self.sn)]

    def exit(self):
        """
        exit command
        """
        return ["exit"]

    def set_description(self, name, address, phone):
        """
        ont description based on customer info
        """
        return ["description %s-%s-%s" % (name, address, phone)]

    def set_profile(self, tcont_num, profile_name):
        """
        tcon number, profile_name
        """
        return ["tcont %s profile %s" % (tcont_num, profile_name)]

    def set_gemport_tcont(self, num, name, tcont_num, mode):
        """
        select gemport
        """
        return ["gemport %s name %s %s tcont %s" % (num, name, tcont_num, mode)]

    def limit_down_gemport(self, gemport_num, value):
        """
        limit gemport traffic down
        """
        return ["gemport %s traffic-limit down %s" % (gemport_num, value)]

    def set_switch_port(self, vlan, vport_num):
        """
        switch vlan to vport
        """
        return ["switchport vlan %s tag vport %s" % (vlan, vport_num)]

    def manage_pon_onu(self, onu_interface):
        """
        onu management
        var: onu_interface
        ex:
            gpon-onu_/1/2/2:1
        """
        return ["Pon-onu-mng %s" % onu_interface]

    def set_flow(self, flow_num, switch):
        """
        set flow
        ex:
            flow 2 switch switch_0/1
        """

        return ["flow %s switch %s" % (flow_num, switch)]

    def set_flow_mode(self, flow_num):
        """
        ex:
            flow mode 1 tag-filter vid-filter untag-filter discard
        """
        return ["flow mode %s tag-filter vid-filter untag-filter discard" % flow_num]

    def set_flow_prority(self, flow_num, priority, vlan):
        """
        ex:
            flow 1  priority 0 vid 602
        """
        return ["flow %s priority %s vid %s" % (flow_num, priority, vlan)]

    def gemport_flow(self, gemport_num, flow_num):
        """
        connecting gemport to flow_num
        ex:
            flow 1 gemport 1
        """
        return ["flow %s gemport %s" % (flow_num, gemport_num)]

    def bind_switch_port_ip_host(self, switch_port, iphost_num):
        """
        binding switch port to ip host
        ex:
            switchport-bind switch_0/1 iphost 1
        """
        return ["switchport-bind %s iphost %s" % (switch_port, iphost_num)]

    def enable_dhcp(self, ip_host_num):
        """
        enable dhcp on ip host
        ex:
            ip-host 1 dhcp-enable true ping-response true traceroute-response true
        """
        return ["ip-host %s dhcp-enable true ping-response true traceroute-response true" % ip_host_num]

    def set_vlan_filter_mode(self, ip_host_num):
        """
        set vlan filter mode
        ex:
            vlan-filter-mode iphost 1 tag-filter untag-filter discard
        """
        return ["vlan-filter-mode iphost %s tag-filter untag-filter discard" % iphost_num]

    def set_vlan_filter_priority(self, ip_host_num, priority, vlan):
        """
        set vlan iphost priority
        ex:
            vlan-filter iphost 1 priority 0 vid 607
        """
        return ["vlan-filter iphost %s priority %s vid %s" % (iphost_num, priority, vlan)]

    def set_vlan_port_eth_mode(self, eth, vlan):
        """
        set vlan port for eth with vlan number
        ex:
            vlan port eth_0/3 mode tag vlan 200
        """
        return ["vlan port %s mode tag vlan %S" % (eth, vlan)]

    def set_dhcp_ip(self, eth):
        """
        set dhcp unicast to eth
        ex:
            dhcp-ip ethuni eth_0/3 from-internet
        """
        return ["dhcp-ip ethuni %s" % eth]

    def set_ssid_name(self, wifi_int, name):
        """
        set ssid name
        ex:
            ssid ctrl wifi_0/1 name Nasa
        """
        return ["ssid ctrl %s name %s" % (wifi_int, name)]

    def set_wpa_key(self, wifi_int, key):
        """
        set wpa key for ssid
        ex:
            ssid auth wpa wifi_0/1 wap2-psk key nasa
        """
        return ["ssid auth wpa %s wpa2-psk key %s" % (wifi_int, key)]

    def hide_ssid(self, wifi_int):
        """
        hide ssid
        ex:
            ssid ctrl wifi_0/2 hide enable
        """
        return ["ssid ctrl %s hide enable" % wifi_int]

    def set_igmp_vlan(self, vlan, gpon_onu, vport ):
        """
        set igmp vlan on gpon onu with vport
        """

        return ["igmp mvlan %s receive-port %s vport %s" % (vlan, gpon_onu, vport)]

    def save_config(self):
        return ["write"]

class CustomCommand:
    def __init__(self):
        self.base = BaseCommand

    def new_olt(self):
        pass