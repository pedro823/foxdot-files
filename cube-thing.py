Scale.default = 'aeolian'
Clock.bpm = 128
Root.default = -0

whitenoise = SynthDef('whitenoise')


def grow(to, how_long=32, fromm=0):
    return linvar([fromm, to], [how_long, inf], start=now)

c1 >> dbass([-1, 6, 6, -1, -1, 7, 7, 0, 0, 7, 0], dur=[1/4, 1/2, 1/4, 1/2, 1/4, 1/2, 1/4, 1/2, 1/4, 1/4, 1/2], lpf=300)
l2 >> bass([-1, 6, 6, -1, -1, 7, 7, 0, 0, 7, 0], dur=[1/4, 1/2, 1/4, 1/2, 1/4, 1/2, 1/4, 1/2, 1/4, 1/4, 1/2], hpf=2000, hpr=0.9)

c2 >> whitenoise([24], dur=[4, rest(28), rest(32)], sus=[4, 28, 32], start=1/2, amp=0.4)

k1 >> play('x ', amp=grow(2))

t1 >> play('n')

print(Samples)

k2 >> print()


