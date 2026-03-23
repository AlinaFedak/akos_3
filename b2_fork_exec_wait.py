import os
import sys

print(f"[Parent] My PID is {os.getpid()}")

pid = os.fork()

if pid == 0:
    print(f"[Child] My PID is {os.getpid()}, executing bash command...")
    os.execlp("bash", "bash", "-lc", "echo 'Hello from child!'; exit 7")
else:
    print(f"[Parent] Waiting for child (PID: {pid}) to finish...")
    child_pid, status = os.waitpid(pid, 0)
    
    exit_code = os.WEXITSTATUS(status)
    print(f"[Parent] Child {child_pid} finished with exit code {exit_code}")
