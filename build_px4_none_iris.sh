#! /bin/bash

# Build the px4 moudles and binaries
make px4_sitl none_iris &> build.log &

# Get the pid of build procsess
PID=$!

msg="Waiting for simulator to accept connection on TCP port 4560"
# Waiting until message will show up in the log file
until grep "$msg" build.log
do
    echo "Waiting for the build process to be done..."
    sleep 3
done

# Kill the make process after the condition is true
kill -INT $PID
echo -e "\nThe build process is done."
