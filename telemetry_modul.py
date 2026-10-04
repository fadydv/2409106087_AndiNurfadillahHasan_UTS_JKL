#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modul: telemetry_modul.py
Tujuan: Menganalisis data sampel telemetry.
Pembuat: Andi Nurfadillah Hasan (2409106087)
"""

# Menggunakan digit NIM (24, 09, 87)
data_telemetry = {
    "router-cabang-1": 24,
    "switch-cabang-1": 87,
    "server-cabang-1": 90
}

def klasifikasi_telemetry():
    print("\n--- Analisis Data Telemetry ---")
    for perangkat, cpu in data_telemetry.items():
        if cpu > 80:
            status = "KRITIS"
        elif 50 <= cpu <= 80:
            status = "WASPADA"
        else:
            status = "NORMAL"

        print(f"Perangkat: {perangkat} | CPU: {cpu}% | Status: {status}")