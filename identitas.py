#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modul: identitas.py
Tujuan: Menyimpan data identitas mahasiswa dan fungsi pembuatan ID perangkat.
Pembuat: Andi Nurfadillah Hasan (2409106087)
"""

nim = "2409106087"
nama = "Andi Nurfadillah Hasan"
kode_cabang = "087"

def buat_id_perangkat(jenis, nomor):
    return f"{jenis}-{kode_cabang}-{nomor}"