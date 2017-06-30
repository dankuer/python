#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Mysocketclient.py
# Created by Dankuer on 2017/7/1

import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('45.32.52.153', 9999))
    print(s.recv(1024).decode('utf-8'))  # 接收欢迎消息
    for data in [b'Dankuer', b'Cosmos', b'DDKK']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
