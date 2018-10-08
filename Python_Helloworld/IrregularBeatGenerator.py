# Omschrijving:
# Audio samples.
# ​​keuze maken uit minimaal twee onregelmatige maatsoorten (bijvoorbeeld 5/4 of 7/8).
# De gebruiker kan ook het tempo in BPM invoeren en optioneel welke sample files gebruikt worden.
# vraagt aan de gebruiker of deze de afgespeelde beat in een file wil bewaren.
# Wanneer de gebruiker de beat wil opslaan dan wordt deze geëxporteerd als MIDI-file.
# Vervolgens wordt er een nieuwe beat gegenereerd en wordt wederom
#
# Wat moet er in het programma komen?
#
# - Input Sectie (Menu), bpm, sample select, maatsoort keuze
# - sequencerpart with generative part
# - Audio Sample Module
# - Midi file Saver
# - Reloop this
#
# Wat heb ik nodig?
#
# - Kennis van Classes, hoe gebruik ik deze en wat kan ik eraan hebben?
# - MultiThreading
# - Kennis van file export-midi functie

from midiutil.MidiFile import MIDIFile
from threading import Thread
import time
import random
import simpleaudio as sa


class Instrument:
    def input(self):
        print("A sound is produced: *Pling* ")

    def midi():

        mf = MIDIFile(1)     # only 1 track
        track = 0   # the only track
        time = 0    # start at the beginning
        channel = 0
        volume = 100

        mf.addTrackName(track, time, "Sample Track")
        mf.addTempo(track, time, 120)

        # add some notes
        pitch = 60           # C4 (middle C)
        time = 0             # start on beat 0
        duration = 1         # 1 beat long
        mf.addNote(track, channel, pitch, time, duration, volume)

        # write it to disk
        with open("output.mid", 'wb') as outf:
            mf.writeFile(outf)

    def sequencer(self):
        print('hommo')




#make an object of this class
myInstrument = Instrument()

#use the makeSound method
myInstrument.makeSound()
myInstrument.makeNoSound()
