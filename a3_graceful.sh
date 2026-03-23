#!/bin/bash

cleanup() {
    echo -e "\n[CLEANUP] Cleaning up temporary files..."
    sleep 1
    echo "[DONE] Exiting gracefully."
    exit 0
}

trap cleanup SIGINT SIGTERM

echo "Process started (PID: $$). Press Ctrl+C to stop me."

tick=1
while true; do
    echo "tick=$tick"
    sleep 1
    ((tick++))
done
