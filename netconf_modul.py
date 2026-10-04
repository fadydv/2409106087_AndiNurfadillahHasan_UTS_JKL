#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modul: netconf_modul.py
Tujuan: Membangun pesan XML NETCONF secara terprogram.
Pembuat: Andi Nurfadillah Hasan (2409106087)
"""

def buat_pesan_netconf():
    vlan_id = "087"

    pesan_xml = f"""
<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> <!-- Messages Layer -->
  <edit-config> <!-- Operations Layer -->
    <target><running/></target>
    <config> <!-- Content Layer -->
      <vlans xmlns="urn:ietf:params:xml:ns:yang:ietf-network">
        <vlan>
          <vlan-id>{vlan_id}</vlan-id>
          <name>VLAN_CABANG_{vlan_id}</name>
        </vlan>
      </vlans>
    </config>
  </edit-config>
</rpc>
"""
    print("\n--- Pesan NETCONF Terprogram ---")
    print(pesan_xml.strip())
    return pesan_xml.strip()