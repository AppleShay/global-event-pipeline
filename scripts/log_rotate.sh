#!/bin/bash

LOG_FILE="/mnt/b/DE/global-event-pipeline/etl_weekly.log"
MAX_SIZE=1048576  # 1MB

if [ -f "$LOG_FILE" ] && [ $(stat -c%s "$LOG_FILE") -gt $MAX_SIZE ]; then
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    mv "$LOG_FILE" "${LOG_FILE}_${TIMESTAMP}.bak"
    gzip "${LOG_FILE}_${TIMESTAMP}.bak"
    touch "$LOG_FILE"
    echo "Log rotated at $TIMESTAMP"
else
    echo "Log not rotated (size too small)"
fi

