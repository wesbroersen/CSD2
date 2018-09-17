RhytmList = []
y = 0

#Import de audio sample
import simpleaudio as sa
from time import sleep


wave_obj = sa.WaveObject.from_wave_file("/Users/wesbroersen 1/Documents/Samples/wijnglas samples/glas water a hard.wav")

#Define the number of playback times
print("numPlaybackTimes: ___________________________")
numPlaybackTimes = input()
#Convert the variable into a integer
numPlaybackTimes = int(numPlaybackTimes)

#Fill a list defined by Playback times with numbers in RhytmList
print("Rhytm: _________________________")
for x in range(0, numPlaybackTimes):
    Rhytm = input()
    float(Rhytm)
    RhytmList.append(Rhytm)

print(RhytmList)

#Define the tempo in the variable called BPM
print("BPM: ___________________________")
BPM = input()
#Convert BPM to floating point value
x = int(BPM)
#Get the BPM in Seconds to work in the delay
BPMMs = 60 / x


play_obj = wave_obj.play()
play_obj.wait_done()

for x in range(0, numPlaybackTimes):


    print(y)
    sleep(BPMMs * float((RhytmList[y])))
    play_obj = wave_obj.play()
    play_obj.wait_done()
    y = y + 1
