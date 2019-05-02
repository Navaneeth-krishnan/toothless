#Main code to begin mission
from dronekit import connect

# Connect to UDP endpoint.
vehicle = connect('127.0.0.1:14550', wait_ready=False)
vehicle.wait_ready(True, timeout=300)
# Use returned Vehicle object to query device state - e.g. to get the mode:
print("Mode: %s" % vehicle.mode.name)