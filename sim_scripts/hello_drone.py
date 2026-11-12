from pymavlink import mavutil

m = mavutil.mavlink_connection('udp:127.0.0.1:14552')
print("Waiting for heartbeat...")
m.wait_heartbeat()
print("Connected: system", m.target_system, "component", m.target_component)

for i in range(5):
    msg = m.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout=5)
    if msg:
        print(f"lat {msg.lat/1e7:.6f}  lon {msg.lon/1e7:.6f}  alt {msg.relative_alt/1000:.1f} m")
