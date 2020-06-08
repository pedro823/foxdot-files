Clock.bpm = 100
Scale.default = 'dorian'
Root.default = 3

pat_a = P[0, 2, 4, 6]
inv_a = pat_a.reverse()[1:]
full_pat_a = pat_a | inv_a | pat_a[1:] | inv_a[:-1]

pat_b = P[1, 3, 4, 5]
inv_b = pat_b.reverse()[1:]
full_pat_b = pat_b | inv_b | pat_b[1:] | inv_b[:-1]

var.pattern = full_pat_a.loop(2) | full_pat_b.loop(2)
var.chords = var([(2, 4, 7, 9), (1, 5, 7, 9)], 8)

a1 >> pluck(var.pattern, dur=1/3, sus=1/8, amp=1, pan=PWhite(-1, 1))
a2 >> ambi(var.chords, dur=1, sus=2, lpf=450, amp=0.15, drive=0.14, room=0.4)

k1 >> play('x', dur=1)
k2 >> play(' ' * 7 + '[ s ]')

k3 >> play(' ' * 5 + 'ss[ s ]', sample=2, rate=1.3)

print(Samples)

bassline = [0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 2]
bassline_dur = [1, 1, 1, rest(2 + 1/4 + 2/3), 3/4, 2/3, 2/3]
a3 >> jbass(bassline, dur=bassline_dur, hpf=200, hpr=0.4, room=0.3)
a4 >> bass(bassline, dur=bassline_dur, lpf=200, lpr=0.8, room=0.3)

a5 >> bass([0, 6, 6, 6, 7], dur=[rest(13 + 2/3), 1/3, 2/3, 2/3, 2/3], sus=1/2)

