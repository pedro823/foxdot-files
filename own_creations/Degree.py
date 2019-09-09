Clock.bpm = 128
Root.default = -5
Scale.default = 'minor'

var.chords = var([0, 0, 3, 2], 4)
var.synth  = var(list(reversed([21, 2, 4, 7, 9, 11, 14, 0])), 1/2)
var.mid = var([-7, -5, -4, 0], 1)
var.bass = var([0, -1], [7, 1])

m1 >> ambi(var.bass - 7, blur=3, lpf=200, dur=[7, 1], drive=0.007, amp=1.1)

s2 >> dirt(var.chords, shape=0.15, lpf=350, lpr=0.9, dur=1, amp=linvar([0, 0.7], [32, inf], start=now))

a2 >> play('m ', hpf=200, amp=linvar([0, 1], [64, inf], start=now))
a3 >> play('x ', lpf=300, lpr=0.5, amp=linvar([0, 0.8], [64, inf], start=now))

a1 >> dbass(var.chords + [0, 0, 7], hpf=600, hpr=0.7, dur=PSum(3, 2), sus=PSum(3, 2), amp=expvar([0, 0.2], [32, inf], start=now))
b1 >> bass(var.chords + [0, 0, 7], dur=PSum(3, 2), lpf=600, lpr=1.1, drive=0.15, fmod=3, amp=expvar([0, 0.1], [32, inf], start=now))

s1 >> blip(var.synth - 7, dur=1/2, sus=1.5, blur=1.5, chop=2, drive=0.1, amp=0.05, room=0.4, mix=0.3)


a4 >> play('[--]', lpf=8000, amp=0.41).stop()

print(Samples)

print(SynthDefs)

a4.stop()
