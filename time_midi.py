from mido import MidiFile
mid = MidiFile('major-scale.mid')
#print(mid.length)
print(mid.tracks)
#print(mid.type)
#for i, track in enumerate(mid.tracks):
#    print('Track {}: {}'.format(i, track.name))
#    for msg in track:
#        print(msg)
