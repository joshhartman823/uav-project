import time
from pymavlink import mavutil

m = mavutil.mavlink_connection('udp:127.0.0.1:14552')
m.wait_heartbeat()
print("Connected")

def set_mode(name):
    m.set_mode(m.mode_mapping()[name])
    time.sleep(1)

def pos():
    msg = m.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout=5)
    return msg

def goto(lat, lon, alt):
    m.mav.set_position_target_global_int_send(
        0, m.target_system, m.target_component,
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
        0b110111111000,
        int(lat * 1e7), int(lon * 1e7), alt,
        0, 0, 0, 0, 0, 0, 0, 0)

set_mode('GUIDED')
m.arducopter_arm()
m.motors_armed_wait()
print("Armed")

m.mav.command_long_send(
    m.target_system, m.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 10)
print("Taking off")
while True:
    p = pos()
    if p and p.relative_alt / 1000 > 9:
        break

for lat, lon in [(-35.362812, 149.165237), (-35.362812, 149.165787)]:
    print("Going to", lat, lon)
    goto(lat, lon, 10)
    time.sleep(25)

print("Returning home")
set_mode('RTL')
