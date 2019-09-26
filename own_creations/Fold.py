Root.default = 5
Scale.default = 'minor'
Clock.bpm = 90

var.melody = var([var([0, 2], 1/2), var([-1, 4], 1/2), var([1, 3], 1/2)], [8, 4, 4])
# F#m, E6 or C#m, Bm
var.chords = var([P(-3, 0, 2, 4), [P(-1, 1, 3, 4), P(1, 3, 4, 6)], [P(-2, 0, 3), P(-2, 0, 3)]], [8, 4, 4])

print(PatternMethods)

print(FxList)

print(Attributes)

s1 >> pluck(var.melody, dur=1/2, amp=1.2).spread()

k1 >> play('x (   O) ', sample=2)

a1 >> ambi(var.melody - 7, dur=1, sus=0.8, blur=0)

p1 >> dirt(var.chords, dur=4, sus=4, amp=0.8).spread()
