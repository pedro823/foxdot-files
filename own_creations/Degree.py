Clock.bpm = 128
Root.default = -5
Scale.default = 'minor'

var.chords = var([0, 0, 3, 2], 4)
var.synth  = var(list(reversed([21, 2, 4, 7, 9, 11, 14, 0])), 1/2)
var.mid = var([-7, -5, -4, 0], 1)
var.bass = var([0, -1], [7, 1])

m1 >> ambi(var.bass - 7, blur=3, lpf=600, dur=[7, 1], drive=0.007, amp=1.1)

s2 >> dirt(var.chords, shape=0.15, lpf=350, lpr=0.9, dur=1, amp=linvar([0, 0.7], [32, inf], start=now))

a2 >> play('m ', hpf=250, amp=linvar([0, 1], [64, inf], start=now))
a3 >> play('x ', lpf=400, lpr=0.5, amp=linvar([0, 0.8], [64, inf], start=now))

a1 >> dbass(var.chords + [0, 0, 0], hpf=600, hpr=0.7, dur=PSum(3, 2), sus=PSum(3, 2), amp=expvar([0, 0.2], [32, inf], start=now))
b1 >> bass(var.chords + [0, 0, 7], dur=PSum(3, 2), lpf=600, lpr=1.1, drive=0.18, fmod=3, amp=expvar([0, 0.15], [32, inf], start=now))

s1 >> blip(var.synth, dur=1/2, sus=1.5, blur=1, chop=2, drive=0.1, amp=linvar([0, 0.07], [32, inf], start=now), room=0.4, mix=0.3)

a2.stop()
a3.stop()
a4.stop()

a1.stop()
b1.stop()

growing = linvar([4, 7], [32, inf], start=now)
n1 >> play('N ', slide=growing, slidefrom=growing-0.1, hpf=linvar([0, 2000], [32, inf], start=now), dur=var([1, 1/2], [16, inf], start=now), amp=linvar([0, 0.3], [4, inf], start=now), rate=0.1)

n1.stop()

a2 >> play('m ', hpf=250, amp=1)
a3 >> play('x ', lpf=400, lpr=0.5, amp=0.9)
a4 >> play('       [ss]', amp=0.3, sample=0)

a4.stop()

s1.stop()

a1 >> dbass(var.chords + [0, 0, [0, 0, 2, -1]], hpf=600, hpr=0.7, dur=PSum(3, 2), sus=PSum(3, 2), amp=0.2)
b1 >> bass(var.chords + [0, 0, [7, 7, 7, -1]], dur=PSum(3, 2), lpf=600, lpr=1.1, drive=0.18, fmod=3, amp=0.15)

m1.stop()
s2.stop()

m1 >> ambi(var.bass - 7, blur=3, lpf=200, dur=[7, 1], drive=0.007, amp=1.2)

s2 >> dirt(var.chords, shape=0.15, lpf=350, lpr=0.9, dur=1, amp=0.7)
