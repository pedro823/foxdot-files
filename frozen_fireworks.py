Clock.bpm = 128
Root.default = 9
Scale.default = 'minor'

var.upper_synth_notes = list(map(lambda x: x+7, [-1, 4, 0, 3] * 4 + [-1, 4, 0, 3, 0, -1, 4, 0, 3]))
var.upper_synth_timing = [1/2, 1, 1/2, 1] * 2 + \
                         [1/2, 1/2, 1/2, 1/2] + \
                         [1/2, 1, 1/2, 1] + [1/2, 1, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2]

var.base_chords = var([(-10, -4, -1, 1, 4), 
                       (-9, -6, 0, 2, 4),
                       (-8, -3, 0, 1, 4),
                       (-7, -4, 0, 2, 4)],
                       [4])
                       
                  
var.bass = var([-10, -9, -8, -7], [3/2, 11/2, 5/2, 13/2])

k1 >> play('<x >', amp=1.2)

a1 >> pluck([0, 0, 7, 0])

b1 >> pluck(var.upper_synth_notes, 
            amp=0.4,
            hpf=1000,
            dur=var.upper_synth_timing)

bk >> pluck(list(map(lambda x: x - 11, var.upper_synth_notes)), dur=var.upper_synth_timing, amp=0.2)

print(SynthDefs)

bc >> bass(var.bass, lpf=180, dur=1/2, blur=1.3, amp=0.5)
