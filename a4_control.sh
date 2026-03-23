#!/bin/bash

echo "1. Starting sleep 100 in background..."
sleep 100 &
pid=$!
echo "   Child PID: $pid"
sleep 1

echo -e "\n2. Sending SIGSTOP..."
kill -STOP $pid
sleep 1
ps u -p $pid

echo -e "\n3. Sending SIGCONT..."
kill -CONT $pid
sleep 1
ps u -p $pid

echo -e "\n4. Terminating process..."
kill -TERM $pid
echo "Process $pid has been terminated."
