#!/usr/bin/env bash
set -e
# Stop any existing server processes
echo "STEP: kill existing python3 app.py if any"
pkill -9 -f "python3 app.py" || true
sleep 0.5
# Start a single instance of the server on port 5000 (no reload)
echo "STEP: start server on 5000 (single instance, no reloader)"
nohup python3 /Users/ronvissers/gamesfromai/app.py > /Users/ronvissers/gamesfromai/server.log 2>&1 &
echo $!
sleep 2
# Show recent log tail for quick verification
tail -n +1 /Users/ronvissers/gamesfromai/server.log | tail -n 60
