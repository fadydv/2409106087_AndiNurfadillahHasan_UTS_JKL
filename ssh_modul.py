#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Modul: ssh_modul.py
Tujuan: Menguji koneksi SSH jarak jauh.
Pembuat: Andi Nurfadillah Hasan (2409106087)
"""
import paramiko

def cek_ssh():
    host_vm = "127.0.0.1"
    port_ssh_vm = 2222
    user_ssh = "admin_087"
    pass_ssh = "dilla087" 

    print("\n--- Mengecek Koneksi SSH ---")
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host_vm, port=port_ssh_vm, username=user_ssh, password=pass_ssh, timeout=5)

        stdin, stdout, stderr = client.exec_command("hostname")
        print("[SSH] Hostname:", stdout.read().decode().strip())

        client.close()
    except Exception as e:
        print("[SSH] GAGAL:", str(e))