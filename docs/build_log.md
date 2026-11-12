# Build Log

## Session 1: Simulation setup and first scripted flight

**Goal:** Get a simulated drone flying waypoints with my own code.

**What I did:**
- Installed WSL2 + Ubuntu 22.04 and built ArduPilot SITL
- Flew a simulated copter by hand: GUIDED mode, arm, takeoff, position commands, RTL
- Wrote a pymavlink script that connects, arms, takes off, flies two waypoints, and returns home

**What went wrong and how I fixed it:**
- Pasted Linux commands into PowerShell instead of Ubuntu. Learned to check the prompt (`PS` = PowerShell, `joshu@...` = Ubuntu).
- Script hung on "Waiting for heartbeat". I had guessed the wrong MAVLink port. Added a dedicated MAVProxy output (`output add 127.0.0.1:14552`) and pointed the script at it.
- "Time moved backwards" warnings from WSL2 clock jitter. Noisy but harmless.
- Pasted multi-line git commands onto one line. Ran them one at a time.

**Next:** Distance-based waypoint checks, GPS/EKF readiness wait, mission upload.
