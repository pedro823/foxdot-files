Clock.bpm = 86
Scale.default = 'minor'
Root.default = 6

var.synth1 = P[7, 0, 1, 2, -7, 2, 1, 0]

p1 >> play('x ')
p2 >> play('       [ss]', sample=1)

s1 >> pluck(var.synth1, dur=1/4)
s2 >> orient(var(-14) + [6, 2, 2, 5, 4, 2, 5, 4], dur=[4, 4, 3/2, 1/2, 2, 3/2, 1/2, 2], lpf=800, room=0.4, mix=0.8)


s3 >> squish([0, 2, 3, 5, 7], dur=PSum(4, 5)).stop()
