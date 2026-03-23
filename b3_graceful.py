import signal
import time
import sys

stop = False

def handler(signum, frame):
    global stop
    print(f"\n[Signal Handler] Received signal {signum}. Setting stop=True...")
    stop = True

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

print("Main loop started. Press Ctrl+C to stop.")

tick = 1
while not stop:
    print(f"tick={tick}")
    time.sleep(1)
    tick += 1

print("[Cleanup] Saving data, closing files...")
time.sleep(1)
print("[Done] Exiting gracefully.")
sys.exit(0)
