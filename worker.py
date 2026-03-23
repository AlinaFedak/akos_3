import signal
import time
import sys

stop = False

def handler(signum, frame):
    global stop
    print(f"\n[Worker] Caught signal {signum}, preparing to stop...")
    stop = True

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

print("[Worker] Started working...")

tick = 1
while not stop:
    print(f"[Worker] tick={tick}")
    time.sleep(1)
    tick += 1

print("[Worker] Cleaned up and stopped.")
sys.exit(0)
