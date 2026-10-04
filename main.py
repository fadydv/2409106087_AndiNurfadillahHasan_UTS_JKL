#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modul: main.py
Tujuan: Integrasi akhir seluruh modul UTS.
Pembuat: Andi Nurfadillah Hasan (2409106087)
"""
import identitas
import ssh_modul
import snmp_modul
import netconf_modul
import telemetry_modul

class LaporanCabang:
    def __init__(self, nim, nama, cabang):
        self.nim = nim
        self.nama = nama
        self.cabang = cabang

    def tampilkan_laporan(self):
        print("="*40)
        print("LAPORAN AKHIR INTEGRASI CABANG")
        print("="*40)
        print(f"Nama   : {self.nama}")
        print(f"NIM    : {self.nim}")
        print(f"Cabang : {self.cabang}")

        ssh_modul.cek_ssh()
        snmp_modul.cek_snmp()
        netconf_modul.buat_pesan_netconf()
        telemetry_modul.klasifikasi_telemetry()
        print("\n" + "="*40)

if __name__ == "__main__":
    laporan = LaporanCabang(identitas.nim, identitas.nama, identitas.kode_cabang)
    laporan.tampilkan_laporan()