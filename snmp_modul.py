#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modul: snmp_modul.py
Tujuan: Mengambil nilai sysName menggunakan SNMPv2c.
Pembuat: Andi Nurfadillah Hasan (2409106087)
"""
from pysnmp.hlapi import (
    SnmpEngine, CommunityData, UdpTransportTarget, ContextData,
    ObjectType, ObjectIdentity, getCmd
)

def cek_snmp():
    host_vm = "127.0.0.1"
    port_snmp_vm = 1161
    community = "comm_087"

    print("\n--- Mengecek Koneksi SNMP ---")
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((host_vm, port_snmp_vm)),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.2.1.1.5.0"))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:
            print("[SNMP] GAGAL:", str(errorIndication))
        elif errorStatus:
            print("[SNMP] GAGAL:", errorStatus.prettyPrint())
        else:
            for vb in varBinds:
                print("[SNMP] sysName:", str(vb[1]))
    except Exception as e:
        print("[SNMP] GAGAL:", str(e))