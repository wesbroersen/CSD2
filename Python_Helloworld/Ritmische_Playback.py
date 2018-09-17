RhytmList = []

#Import de audio sample
import simpleaudio as sa
from time import sleep


wave_obj = sa.WaveObject.from_wave_file("/Users/wesbroersen 1/Documents/Samples/rhythm-lab.com_amen_vol.1/WAV/cw_amen01_175.wav")

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

#Define the tempo in the variable called BPM
print("BPM:")
BPM = input()
#Convert BPM to floating point value
x = int(BPM)
#Get the BPM in Seconds to work in the delay
BPMMs = 60 / x

print(BPMMs)



number = 0

for x in range(0, numPlaybackTimes):

    play_obj = wave_obj.play()
    play_obj.wait_done()

    sleep(RhytmList[# hier moet het getal uit the Rhytmlist komen die bepaald hoeland de sleep functie moet werken ])
