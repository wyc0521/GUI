# script to test all remote commands of IOSONO inside
# preparation to fully functional easy control

import iosono_inside_remote_commands
import socket
import time

########################
###   MAIN PROGRAM   ###
########################

# connection parameter like IP address and port of the processor    
hostIP = "192.168.178.27"
portNumber = 4444 # must be integer
connectionType = "UDP"

print ("Host ip address:", hostIP)
print ("Target port:", portNumber)
print ("Type:", connectionType)
print ("-------------------------")

# ii is an object with all the remote contol functionality
ii = iosono_inside_remote_commands


# establish communication
ii.setHost(hostIP)
ii.setPort(portNumber)
ii.createSocket(connectionType)

##if connectionType == "TCP":
##    ii.tcpConnect()


# main loop
while ii.ping():
    print("YES, I can ping the machine")
##    currPres = ii.getCurrentPreset()
##    print("Name of current Preset: ", currPres)
##    currState = ii.getState()
##    print("State: ",currState)
##    currVol = ii.getVolume()
##    print("Volume: ",currVol)
    nPres = ii.getNumberOfPresets()
    #print("Number of Presets: ",nPres)
##    presetList = ii.getPresetList()
##    print("Preset List:\n",presetList)
    time.sleep(3)

# if ping is not True, end of the main loop
print("NO, I cannot ping the machine")

##if connectionType == "TCP":
##    ii.tcpClose()
