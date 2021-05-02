import time
import numpy
import json

# pypot imports
import pypot.dynamixel

ports = pypot.dynamixel.get_available_ports()

if not ports:
    raise IOError('no port found!')

print('ports found', ports)

print('connecting on the first available port:', ports[0])
dxl_io = pypot.dynamixel.DxlIO(ports[0], baudrate=57600)

ID = 1
print("Test with PID only:")

dxl_io.enable_torque({ID: 1})
time.sleep(0.1)
dxl_io.set_goal_position({ID: 0})
time.sleep(1)
# dxl_io.set_pid_gain({ID: [1, 0, 0]})
# time.sleep(0.1)
