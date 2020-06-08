Clock.bpm = 128
Root.default = 3
Scale.default = 'major'

def grow(to, how_long=32, fromm=0):
   return linvar([fromm, to], [how_long, inf], start=now)

p1 >> play('x ', hpf=200, amp=1.1)
p2 >> play(' ' * 15 + '[ss]', sample=1, rate=2).spread()

primary_pattern = PSum(4,3)[:21] | P[0.25]
offbeat_pattern = list(rest(8) | PSum(4,3)[:10] | P[0.5])

C_minor = (-2, 0, 2)
Ab_major = (-4, -2, 0)
Eb_major = (-5, -3, 0)

s1 >> pluck([3, 3, 2, 2] + [0] * 7 + [0] * 8 + [-1] * 3, 
    dur=primary_pattern, 
    amp=0.3).spread()
s2 >> pluck([C_minor for _ in range(22)] 
        + [Ab_major for _ in range(16)] 
        + [Eb_major for _ in range(6)], 
        dur=primary_pattern, 
        lpf=400, 
        amp=0.3).spread()
s3 >> pluck([0, 2, 2, 0, 1, -1, -1, -1, -1, -1, -1, -1], 
    dur=offbeat_pattern,
    amp=0.3).spread()
