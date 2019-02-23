#!/bin/bash

cd "$(dirname "$0")"

checkmodule -M -m -o torque_adopt.mod torque_adopt.te || exit 1
semodule_package -o torque_adopt.pp -m torque_adopt.mod || exit 2
semodule -i torque_adopt.pp || exit 3
