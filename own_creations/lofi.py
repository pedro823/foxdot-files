Scale.default = 'minor'
Root.default = -3
Clock.bpm = 140

d1 >> play('<(x )   d   ><    +  ( -)>')

d3 >> play('n N s ', rate=PRange(1, 5), sample=PRand(5), pan=PWhite(-1, 1), lpf=2000, dur=1/4, amp=0.7).spread()

c1 >> soft([(0, 2), (0, 2), (3, 5), (2, 4)], dur=4).offbeat(4)

print(SynthDefs)
