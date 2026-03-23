import subprocess
import time

MAX_RESTARTS = 3
restarts = 0

print("[Supervisor] Starting...")

while restarts < MAX_RESTARTS:
    print(f"\n[Supervisor] Launching worker (Attempt {restarts + 1}/{MAX_RESTARTS})")
    
    proc = subprocess.Popen(["python3", "worker.py"])
    
    proc.wait()
    
    print(f"[Supervisor] Worker exited with code {proc.returncode}")
    restarts += 1
    time.sleep(1)

print("[Supervisor] Reached MAX_RESTARTS. Shutting down.")
