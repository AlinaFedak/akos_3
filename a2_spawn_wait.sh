#!/bin/bash

echo "Starting child process in background..."
( sleep 2; exit 7 ) &
child_pid=$!

echo "Child process started with PID: $child_pid"
echo "Waiting for child to finish..."

wait $child_pid
exit_code=$?

echo "Child finished. Exit code: $exit_code"
