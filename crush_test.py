Clock.bpm = 128
Root.default = 5

d1 >> play('m m(       m)', hpf=220, hpr=0.7)
d2 >> play('x x ', crush=8, dist=0.1)

a1 >> pluck([0, 3, 4, 5], crush=5)
