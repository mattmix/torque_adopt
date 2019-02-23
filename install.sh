#!/bin/bash

cd "$(dirname "$0")"

cp torque_adopt_socket /usr/sbin/torque_adopt_socket
cp torque_adopt /usr/sbin/torque_adopt
chmod 700 /usr/sbin/torque_adopt_socket
chmod 700 /usr/sbin/torque_adopt

cp torque_adopt.socket /etc/systemd/system
cp torque_adopt@.service /etc/systemd/system
systemctl daemon-reload

systemctl enable torque_adopt.socket
systemctl start torque_adopt.socket

