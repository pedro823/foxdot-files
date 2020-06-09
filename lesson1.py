Clock.bpm = 128

Scale.default = 'minor'
Root.default = -3

k1 >> play('x ', sample=1, amp=1.2)
k2 >> play(' [|s2||s4|]|-5|s', amp=0.3, rate=1.2)

s1.stop()

# boring :(
bassline = P[0, -7, 0, 2]

s1 >> pluck(bassline, dur=1/2)

# offbeat
s1 >> pluck(bassline).offbeat()

# offbeat + stutter!
s1 >> pluck(bassline).offbeat().every(8, 'stutter', amount=4, dur=1)

s1.stop()

# so much cooler
Clock.bpm = 128
polirhythm_bassline = P[0, -7, 0, 2, 0, -7, 0, 2, 0, -7, 0]

print(PSum(4,3))

print(PSum(4, 3)[:10] | P[0.5])

# inspired on deadmau5 - polaris,
s1 >> pluck(polirhythm_bassline, dur=PSum(4, 3)[:10] | P[0.5])

# used on many songs, e.g. No Mana & Jantine - Strangers
s1 >> pluck(P[[0] * 9] | P[1, -1], root=1, dur=PSum(4, 3)[:10] | P[0.5])

# you can offset some of the notes for even greater effect
s1 >> pluck(polirhythm_bassline, dur=PSum(4, 3)[:8] | P[1, 0.5, 0.5])

# No Mana & Cafcat - Lethargy
s1 >> pluck([0, -7, -1, 1, -1, 0], dur=[0.5, 0.75, 0.75, 0.75, 0.75, 0.5], root=5)

# Digitalism - Miami Showdown
Clock.bpm = 95
s1 >> pluck([7, 3, 4, 5, 6, 7], dur=PSum(4, 3)[:4] | P[0.5, 0.5], root=0)

# remember to rest!
rested_bassline = P[-7, -7, -7, -7, -7, 0]
Clock.bpm = 128

print(PSum(5, 3)[:5])
print(sum(PSum(5, 3)[:5]))

five_three_pattern = PSum(5, 3)[:5].shuffle()

s1 >> pluck(rested_bassline, dur=five_three_pattern | rest(1))

# with rests, equal intervals also sound cool
equal_intervals = P[[0.5] * 5]

s1 >> pluck(rested_bassline, dur=equal_intervals | rest(1.5)) # looks like deadmau5 - sofi needs a ladder!

# Tresillo! Go latin america :)
Clock.bpm = 110

s1 >> pluck(-7, dur=PSum(3, 2))

# Tresillo three-two
s1 >> pluck(-7, dur=P[0.75, 0.75, 1, 0.5, 1], sus=0.5)

# moombahton/reggaeton pattern
s1 >> pluck(-7, dur=rest(0.75) | P[0.75, 0.25] | rest(0.25), sus=0.5)

# You can go super complex!
# This is a recreation of the second drop of Jason Ross & Melanie Fontana - Shelter (No Mana remix)
Root.default = 3
Scale.default = 'major'
Clock.bpm = 128
k1 >> play('x ', hpf=200, amp=1.1)
k2.stop()
primary_pattern = PSum(4,3)[:21] | P[0.25]
offbeat_pattern = rest(8) | PSum(4,3)[:10] | P[0.5]
C_minor = (-2, 0, 2)
Ab_major = (-4, -2, 0)
Eb_major = (-5, -3, 0)
s1 >> pluck([3, 3, 2, 2] + [0] * 7 + [0] * 8 + [-1] * 3,
    dur=primary_pattern,
    amp=0.3).spread()
s2 >> pasha([C_minor for _ in range(22)]
        + [Ab_major for _ in range(16)]
        + [Eb_major for _ in range(6)],
        dur=primary_pattern,
        lpf=400,
        amp=0.3).spread()
s3 >> pluck([0, 2, 2, 0, 1, -1, -1, -1, -1, -1, -1, -1],
    dur=offbeat_pattern,
    amp=0.3).spread()
