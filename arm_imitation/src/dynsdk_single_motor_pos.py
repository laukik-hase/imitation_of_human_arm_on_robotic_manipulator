import time
import arm_control_utils

# offset = [180 180 90] # niryo
# DXL_ID = [1,2,3]
DXL_ID = [1]

my_arm_controller = arm_control_utils.arm_controller(DXL_ID,devicename='/dev/ttyUSB0', baudrate=1000000)



my_arm_controller.initialize_motors()
my_arm_controller.enable_state_torque()

# state = [2560]
state = [3072]
my_arm_controller.write_state(state)
time.sleep(2)

# state = [1024]
# my_arm_controller.write_state(state)
# time.sleep(2)

my_arm_controller.disable_state_torque()
my_arm_controller.stop_motors()