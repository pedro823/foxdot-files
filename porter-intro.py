Root.default = 3
Clock.bpm = 90

var.chords = var([4, 1, 0, [5, var([0, -1], [2, 2])]])

at >> swell(var.chords, dur=2, amp=1.2)

b1 >> jbass(var.chords, dur=4)

b2 >> sinepad(var.chords, dur=2, amp=1)

pr >> pasha([9,7,6,4,2,0] * 2 + [9,7,6,4], dur=1/4)

d1 >> play('x', dur=1/4, amp=1.3)

d1.stop()
at.stop()
pr.stop()

var.chords = var([0])

d1 >> play('x   ', amp=1.2)

b1.stop()

var.synth = var([0, 0, 0, 4, 2, 4, 2, 1], [5/6, 5/6, ])
