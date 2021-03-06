#!/usr/bin/env python

from midiutil import MIDIFile

# degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
degrees = [65] * 3600
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1, file_format=0)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("test.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
