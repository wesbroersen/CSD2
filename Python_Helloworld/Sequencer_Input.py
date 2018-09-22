import simpleaudio as sa
import time
import random
import threading

# Why is this code more accurate than the previous sleep examples?
#
# Because when the time stamps match the internal clock whatever happens they
# will play where as the other examples stop the code and aren't running
# while this happens. The internal clock however is in this example always running
# (and quite on time as wel).


# load 1 audioFile and store it into a list
# note: using a list taking the next step into account: using multiple samples
samples = [sa.WaveObject.from_wave_file("wijnglas samples/WijnglasA.wav"),
sa.WaveObject.from_wave_file("wijnglas samples/WijnglasB.wav"),
sa.WaveObject.from_wave_file("wijnglas samples/WijnglasC.wav")]

noteDuration = []

"""
Rotating function

def rotate(l, x):
  return l[-x:] + l[:-x]

rotate(timestamps, 1)
"""


timestamps16th = []
def convertToTimestamps(noteDuration):
    y = 0
    for note in noteDuration:
        x = note * 4
        timestamps16th.append(x + y)
        y = timestamps16th[-1]






#set BPM and convert first convert it to the quarternote duration in Seconds
#than divide it by 4 to get sixteenth note duration for the smallest number
print("BPM: ____________________________________")
bpm = int(input())
quarterNoteDuration = 60 / bpm
sixteenthNoteDuration = quarterNoteDuration / 4.0

# Declare the length of the rhytm list
print("LengthRhytm: ____________________________")
lengthRhytm = int(input())

#Fill in the list u just declared in length
print("Timestamps: _____________________________")
for x in range(0, lengthRhytm):
    noteDuration.append(float(input()))


#Say how many times u want to run the entire script
print("Amount of Cycles: _______________________")
amount = int(input()) + 1




for x in range(0, amount):
    # create a list to hold the timestamps
    timestamps = []
    timestamps16th = []


    # create a list with ‘note timestamps' in 16th at which we should play the sample

    # noteDuration = [1,1,1,1]
    convertToTimestamps(noteDuration)






    # transform the sixteenthTimestamps to a timestamps list with time values
    for timestamp in timestamps16th:
      timestamps.append(timestamp * sixteenthNoteDuration)

    # retrieve first timestamp
    # NOTE: pop(0) returns and removes the element at index 0
    timestamp = timestamps.pop(0)

    # retrieve the startime: current time






    startTime = time.time()
    keepPlaying = True

    while keepPlaying:
      # retrieve current time
      currentTime = time.time()

      # print(currentTime)
      # check if the timestamp's time is passed
      if(currentTime - startTime >= timestamp):
        # play sample
        randomSample = random.randint(0, 2)
        samples[randomSample].play()
        print("sample")

        # if there are timestamps left in the timestamps list
        if timestamps:
          # retrieve the next timestamp
          timestamp = timestamps.pop(0)

        else:
          # list is empty, stop loop
          keepPlaying = False
      else:
        # wait for a very short moment
        time.sleep(0.001)
