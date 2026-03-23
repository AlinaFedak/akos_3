import os
import subprocess

pid = os.getpid()
ppid = os.getppid()

print(f"PID: {pid}")
print(f"PPID: {ppid}")
print("-" * 30)

subprocess.run(["ps", "u", "-p", str(pid)])
