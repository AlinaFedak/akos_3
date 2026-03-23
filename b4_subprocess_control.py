import subprocess
import signal
import time
import os

print("1. Starting sleep 100...")
proc = subprocess.Popen(["sleep", "100"])
print(f"   Child PID: {proc.pid}")
time.sleep(1)

print("\n2. Sending SIGSTOP...")
proc.send_signal(signal.SIGSTOP)
time.sleep(1)
os.system(f"ps u -p {proc.pid}")

print("\n3. Sending SIGCONT...")
proc.send_signal(signal.SIGCONT)
time.sleep(1)
os.system(f"ps u -p {proc.pid}")

print("\n4. Terminating...")
proc.terminate()
proc.wait()

print(f"Process finished. Return code: {proc.returncode}")
