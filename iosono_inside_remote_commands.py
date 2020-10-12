# script to test all remote commands of IOSONO inside
# preparation to fully functional easy control

import socket
import time

# definition of the remote control commands as python functions
# still under construction

## create a TCP socket
#sock = socket.socket(socket.AF_INET, # Internet
#                     socket.SOCK_STREAM) # TCP


socket.setdefaulttimeout(5)
sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP
connectionType = "UDP"

def setHost(h):
    global HOST
    HOST = h
    print("HOST is set to:" + HOST)
    return True

def setPort(p):
    global PORT
    PORT = p
    print("PORT is set to:" + str(PORT))
    return True

#---------- TPC --------------------------------   
def connect():
# establish connection
    try:
        sock.connect((HOST, PORT))
        print("Connection established")
        return True
    except:
        print("Connection failed")
        return False

def close():
# close connection
    sock.close() # close the TCP connection
#-------------------------------------------------
    
def ping():
# returns True when Machine is online and answers with OK, otherwise False
    #print("Try to ping the machine: " + HOST + " on port: " + str(PORT))
    try:
        # test if the machine is online
        sock.sendto(bytes("ping \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        #print("Machine is ONLINE")
        if ":OK:" in answer:
            #print("Machine is OK")
            return True
        else:
        #elif print("Machine is not OK"):
            return False
    except:
        print("Machine seems to be OFFLINE...")

def startPresetByName(presetName):
# call the function with a string argument
# function tries to start the preset by this name
    try:
        sock.sendto(bytes("controlunit/set_preset " + presetName + "\r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        if  ":OK:" in answer:
            print("Preset with name '" + presetName + "' is starting...")
            return True
        else:
            print("Preset with name '" + presetName + "' could not be started")
            return False
    except:
        print("No answer for startPresetByName(presetName)")
        
def startPresetByNumber(presetNumber):
# call the function with an integer number argument (starting with 1, not 0)
# function tries to start the preset by this number
    try:
        sock.sendto(bytes("controlunit/set_preset_nr " + str(presetNumber) + "\r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        if ":OK:" in answer:
            print("Preset No." + str(presetNumber) + " is starting...")
            return True
        else:
            print("Preset No." + str(presetNumber) + " could not be started.")
            return False
    except:
        print("No answer for startPresetByName(presetName)")

def getCurrentPreset():
# returns a string with the name of the currently running preset
# if string is empty, no preset is running
    #print("ask for current preset")
    try:
        sock.sendto(bytes("controlunit/get_current_preset \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        msg = sock.recv(4096)
        #print(msg)
        answer = str(msg, "utf-8")
        #print(answer)
        if ":OK:" in answer:
            #print("Command getCurrentPreset() successful")
            currPreset = answer.split('\r\n') # removes line break and carriage return
            currPreset.pop() # removes very last, empty line
            currPreset.remove(":OK:") # removes the command status :OK:
            return currPreset[0]
        else:
            #print("Command getCurrentPreset() not successful")
            return False
    except:
        print("No answer for getCurrentPreset()")

def getPresetList():
#returns a list with all preset names
    try:
        sock.sendto(bytes("controlunit/get_all_presets \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        if ":OK:" in answer:
            presetList = answer.split('\r\n') # removes line break and carriage return
            presetList.pop() # removes very last, empty line
            presetList.remove(":OK:") # removes the command status :OK: 
            return presetList
        else:
            print("Command getPresetList() not successful")
    except:
        print("No answer for getPresetList()")

def getNumberOfPresets():
# returns the number of presets as integer value
    try:
        sock.sendto(bytes("controlunit/get_nr_of_presets \r\n", "utf-8"), (HOST, PORT))
        msg = sock.recv(4096)
        #print(msg)
        answer = str(msg, "utf-8")
        #print(answer)
        presetCount = answer.split('\r\n') # removes line break and carriage return
        if presetCount[0].isdigit():
            #print("Command getNumberOfPresets() successful")
            return int(presetCount[0])
        else:
            #print("no digit")
            return False
    except:
        print("No answer for getNumberOfPresets()")

def getState(currPreset):
# returns status in colors black, green, red, yellow    
    if currPreset == "": # reads global variable currPreset
        state = "black"
        return state
    else:
        #print("ask machine for state")
        try:
            # get the machine state
            sock.sendto(bytes("controlunit/get_state \r\n", "utf-8"), (HOST, PORT))
            answer = str(sock.recv(4096), 'utf-8')
            if ":STATE_OK:" in answer:
                state = "green"
                return state
            elif ":STATE_ERROR:" in answer:
                state =  "red"
                return state
            elif ":STATE_WARNING:" in answer:
                state =  "yellow"
                return state
        except:
            print("No status available")
    # states are :STATE_OK: or :STATE_WARNING: or :STATE_ERROR:

def setVolume(dbValue):
    sock.sendto(bytes("controlunit/set_volume " + str(dbValue) +"\r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    if ":OK:" in answer:
        print("Volume has been set")
    elif print("Volume could not be set"):
        return answer

def getVolume():
    sock.sendto(bytes("controlunit/get_volume \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    volume = float(answer.replace("\r\n", ""))
    return volume

def stopCurrentPreset():
    # stop the currently running preset
    sock.sendto(bytes("controlunit/stop_current_preset \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    if ":OK:" in answer:
        print("Preset has stopped")
        return True
    elif print("Preset could not be stopped"):
        return False

def getFilterConfigs(presetName):
    # get the list of items in the current filter config list matching the preset
    filterConfigList = []
    sock.sendto(bytes("controlunit/get_filter_configs " + str(presetName) + "\r\n", "utf-8"), (HOST, PORT))
    filterConfigList = str(sock.recv(4096), 'utf-8')
    filterConfigList = filterConfigList.replace("\r\n", "")
    print("=== Filter configs === \n" + filterConfigList + "\n===")

def setFilterConfig(filterConfigName):
    # set (or select) the filter config for the running preset
    sock.sendto(bytes("controlunit/set_filter_config " + str(filterConfigName) + "\r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer

def shutdown():
    sock.sendto(bytes("system/shutdown \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer

def playerPlay():
    sock.sendto(bytes("player/play \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer

def playerStop():
    sock.sendto(bytes("player/stop \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer

def playerPause():
    sock.sendto(bytes("player/pause \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer

def getTracklist():
    # get the list of items in the current preset's playlist
    sock.sendto(bytes("player/get_tracklist \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    print(answer)
    # write the names in a list
    playlist = answer.split('\r\n')
    playlist.pop() # removes very last, empty line
    playlist.remove(":OK:") # removes the line with :OK: as it is no preset
    print("Found", len(playlist), "items in the playlist...")

def getNumberOfTracks():
    sock.sendto(bytes("player/get_nr_of_tracks \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer

def setTrack(trackNumber):
    # set (or select) the track by its number in the list of presets
    sock.sendto(bytes("controlunit/set_preset_nr " + str(trackNumber) + "\r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    if ":OK:" in answer:
        print("Track No." + str(trackNumber) + " is selected...")
    elif print("Track could not be set"):
        return answer

def setLoopmode(loopmode):
    sock.sendto(bytes("player/set_loopmode " + str(loopmode) + "\r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    # loopmodes are: play_one, play_all, repeat_one, repeat_all
    mode = answer.split('\r\n')
    mode.pop() # removes very last, empty line
    mode.remove(":OK:") # removes the line with :OK: as it is no preset
    return mode

def getLoopmode():
    sock.sendto(bytes("player/get_loopmode \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer
    print(answer)

def getTrackLength():
    # track length in sec
    sock.sendto(bytes("player/get_tracklength \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer
    print(answer)
    
def getPlaybackState():
    try:
        # get the playback state
        sock.sendto(bytes("player/get_playbackstate \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        #print(answer)
        return answer
    except:
        print("No status available")
    # playback states are :PLAYING: or :PAUSED: or :STOPPED:
    # if no player preset is running a message :EXECUTION_ERROR: is received

def setPosition(progress):
    # progress is from 0 to 100 percent of the duration
    sock.sendto(bytes("player/set_position " + str(progress) + "\r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')


def getPosition():
    # from 0 to 100 percent of the duration
    sock.sendto(bytes("player/get_position \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    print(answer)
    answer = answer.replace("\r\n:OK:", "")
    print(answer)
    return answer



'''
HOST = "192.168.178.34"
PORT = 4444

print ("Host ip address:", HOST)
print ("Target port:", PORT)
print ("-------------------------")



socket.setdefaulttimeout(5)
sock = socket.socket(socket.AF_INET,  # Internet
                              socket.SOCK_DGRAM)  # UDP
connectionType = "UDP"

print(ping())

while ping():
    
    currPreset=getCurrentPreset()
    print(currPreset)
    print(getState(currPreset))

'''










