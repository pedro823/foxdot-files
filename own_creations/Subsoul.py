Root.default = 4
Scale.default = 'minor'
Clock.bpm = 122

var.bass = var([0, 0, 0, 2], 4)

def grow(to, how_long):
    return linvar([0, to], [how_long, inf], start=now)

w1 >> ambi(var.bass - 21, amp=1.2, rate=3, dur=2).spread()

k1 >> play('x ', rate=0.9, amp=grow(1.2, 32))
k2 >> play('m ', rate=1, sample=1, hpf=400, amp=grow(1.2, 32)).spread()
sh >> play(' ' * 15 + '[NN]', rate=3, amp=grow(1, 32))

w2 >> ambi(var.bass - 21, 
           dur=[rest(1/2), 2, rest(3/2)], 
           amp=1.2, 
           drive=0.1, 
           chop=2, 
           lpr=0.5, 
           lpf=240, 
           fmod=0).spread(0.2).slider().every(8, 'bubble')
           
e1 >> play(' ' * 31 + '-', rate=0.1, hpf=450, amp=0.8, delay=-0.05, room=0.3, mix=0.3).spread()
s1 >> pluck(16, dur=[rest(15 + 1/2), 1/2], slide=0.2, sus=1/4, amp=0.4).spread()

s2 >> arpy(var.bass + [14, 14, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0], amp=expvar([0, 0.4], [32, inf], start=now), dur=[1, 1] + [1/2] * 12, sus=1/2).slider().every([64], 'reverse').every(6, 'stutter', 4, dur=1/2)



