#!/bin/bash

echo "Current Process ID (PID): $BASHPID"
echo "Parent Process ID (PPID): $PPID"
echo -e "\nDetailed info from ps:"

ps u -p $BASHPID

