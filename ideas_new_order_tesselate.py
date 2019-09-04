Clock.bpm = 120
Root.default = 2
Scale.default = "minor"

d2 >> pluck([0, 2, 1], dur=1)

d1 >> play("<x x ><--(   [---])->", sample=(0, 1))

b1 >> bass([0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 3, -1, -1, -1, 0], amp=1, dur=1/2)

p2 >> blip([0, 0, 0, 0, 0, 0, 0, 0, 0, 0] + [2, 2, 2] + [3, -1, -1], dur=[1/2, 1/4, 1/4]).stop()

d1 >> play('<x---u---><|s1|       >', dur=[1/4, 1/2, 1/2, 3/4, 1/2, 1/2, 1/2, 1/2], amp)

print(Samples)

d1.stop()
d2 >> play('x       ')

d2.stop()
d3 >> play('x   u   ' * 3 + '    u   ').stop()
