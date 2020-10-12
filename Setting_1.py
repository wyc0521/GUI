# script to test all remote commands of IOSONO inside
# preparation to fully functional easy control

import socket
import time




# definition of the remote control commands as python functions
# still under construction
# use exceptions


socket.setdefaulttimeout(5)
sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP




def setHOST(hostName, portName):
    global HOST, PORT
    HOST = hostName
    PORT = portName


def ping():
    try:
        # test if the machine is online
        sock.sendto(bytes("ping \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        #print("Machine is ONLINE")
        return True
    except:
        #print("Machine seems to be OFFLINE...")
        return False





def startPresetByName(presetName):
    # set the preset by its name
    sock.sendto(bytes("controlunit/set_preset " + presetName + "\r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    if  ":OK:" in answer:
        print("Preset with name '" + presetName + "' is starting...")
    elif print("Preset could not be started"):
        return answer

def startPresetByNumber(presetNumber):
    # set the preset by its number in the list of presets
    sock.sendto(bytes("controlunit/set_preset_nr " + str(presetNumber) + "\r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    if ":OK:" in answer:
        print("Preset No." + str(presetNumber) + " is starting...")
    elif print("Preset " + str(presetNumber) + " could not be started. Check number of presets."):
        return answer

def getCurrentPreset():
    try:
        # get the machine state
        sock.sendto(bytes("controlunit/get_current_preset \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        currPreset = answer.split('\r\n')  # removes line break and carriage return
        currPreset.pop()  # removes very last, empty line
        currPreset.remove(":OK:")
        return currPreset[0]
    except:
        #print("No current preset request possible")
        return

def getPresetList():
# returns a list with all preset names
    try:
        sock.sendto(bytes("controlunit/get_all_presets \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        if ":OK:" in answer:
            presetList = answer.split('\r\n')  # removes line break and carriage return
            presetList.pop()  # removes very last, empty line
            presetList.remove(":OK:")  # removes the command status :OK:
            return presetList
        else:
            #print("Command getPresetList() not successful")
            return
    except:
        #print("No answer for getPresetList()")
        return


def getNumberOfPresets():
    sock.sendto(bytes("controlunit/get_nr_of_presets \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    return answer

def getState():
    try:
        # get the machine state
        sock.sendto(bytes("controlunit/get_state \r\n", "utf-8"), (HOST, PORT))
        answer = str(sock.recv(4096), 'utf-8')
        return answer
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
    elif print("Preset could not be stopped"):
        return answer

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
    print(answer)
    return answer


def getTrackLength():
    # track length in sec
    sock.sendto(bytes("player/get_tracklength \r\n", "utf-8"), (HOST, PORT))
    answer = str(sock.recv(4096), 'utf-8')
    print(answer)
    return answer

    
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


########################
###   MAIN PROGRAM   ###
########################

# connection parameter like IP address and port of the processor

#
# HOST = "192.168.178.27"
# PORT = 4444
# #
# print ("Host ip address:", HOST)
# print ("Target port:", PORT)
# print ("-------------------------")
#
#
# #
# socket.setdefaulttimeout(5)
# sock = socket.socket(socket.AF_INET,  # Internet
#                              socket.SOCK_DGRAM)  # UDP
#
# example calls of various functions to test
#
# test: ping the machine and print the answer
# print(ping())

#PASSED

#print('Current Volume is: ' + str(getVolume()) + ' dB')

# print(getCurrentPreset())
# print(getVolume())

#print(getState())

#startPresetByNumber(1)

#setVolume(-2)

# test: show the status of the machine
#print("IOSONO inside state (ok, warning, error): ", getState())
# PASSED

#print(setFilterConfig("20191010_Kunming_SeatPos_v1"))

# getPresetList()
#print(getNumberOfPresets())
#getFilterConfigs('IMF')

# test 3: start a preset by number
#startPresetByNumber(1)
#print("Current preset: ", getCurrentPreset())
# FORMATTING the return variable to a string needed (no :OK: feedback status or new lines)

#shutdown()