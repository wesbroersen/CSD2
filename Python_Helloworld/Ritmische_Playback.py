RhytmList = []

#Import de audio sample
import simpleaudio as sa


wave_obj = sa.WaveObject.from_wave_file("/Users/wesbroersen 1/Documents/Samples/rhythm-lab.com_amen_vol.1/WAV/cw_amen01_175.wav", 2, 2, 44100)

#Define the number of playback times
print("numPlaybackTimes:")
numPlaybackTimes = input()
#Convert the variable into a integer
numPlaybackTimes = int(numPlaybackTimes)

#Fill a list defined by Playback times with numbers in RhytmList
print("Rhytm:")
for x in range(0, numPlaybackTimes):
    Rhytm = input()
    float(Rhytm)
    RhytmList.append(Rhytm)

x = len(RhytmList)
print(x)

#Define the tempo in the variable called BPM
print("BPM:")
BPM = input()
float(BPM)








#for x in RhytmList:
#  print(x)
#Converteren van de String input naar float value's





for x in range(0, numPlaybackTimes):
    play_obj = wave_obj.play()
    play_obj.wait_done()
