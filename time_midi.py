from mido import MidiFile
mid = MidiFile('test.mid')
print(mid.length)
print(mid.tracks)
print(mid.type)
#for i, track in enumerate(mid.tracks):
#    print('Track {}: {}'.format(i, track.name))
#    for msg in track:
#        print(msg)
