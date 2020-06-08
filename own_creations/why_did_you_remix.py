Scale.default = 'mixolydian'
Root.default = -3
Clock.bpm = 120

### Drums ###

# aux player definitions
ss2 = Player()
ss3 = Player()
sn2 = Player()
sn3 = Player()

k1 >> play('^       ', lpf=150, rate=0.4, pan=0.2)
k2 >> play('x       ', bpf=250, bpr=1.2, pan=-0.2)

beat_one_kicks = Group(k1, k2)
beat_one_kicks.amp = 1

shaker_pattern = ' [s {s } ]  {ss }{ss } s'

ss  >> play(shaker_pattern, rate=2, drive=0.1, pan=PWhite(-1, 1)).spread()
ss2 >> play(shaker_pattern.replace('s', 'n'), amp=0.3, pan=PWhite(-1, 1)).spread()
ss3 >> play(shaker_pattern, rate=3, sample=1, pan=PWhite(-1, 1)).spread()

shakers = Group(ss, ss2, ss3)

drums.amp = 1

snare_pattern = '    +   '

sn >> play(snare_pattern, bpf=2000, bpr=0.3).spread()
sn2 >> play(snare_pattern.replace('+', 'p'), drive=0.1, rate=3, sample=2).spread()

snares = Group(sn, sn2)

pre_snare_pattern = '   [ { s-}]    '

sn3 >> play(pre_snare_pattern, bpf=1900, amp=1.2, rate=0.9, pan=PRand(-1, 1))

snap_pattern = ' {h }      '

fx >> play(snap_pattern, rate=1.05, amp=1, pan=PWhite(-1, 1), sample=0)

middle_kick_pattern = '     [ ^ ] ^'

k3 >> play(middle_kick_pattern).stop()

s1 >> stretch("why_did_you_beat2_120BPM.wav", dur=8, amp=0.4, pan=0)

beat_samples = Group(s1)

drums = Group(beat_one_kicks, snares, shakers, beat_samples, sn3, fx, s1)

def open_your_eyes():
    op_yr_iz = Player()
    drums.amp = 1
    op_yr_iz >> stretch("why_did_you_open-your-eyes_120BPM.wav", dur=4).solo()
    Clock.schedule(op_yr_iz.solo, Clock.now() + 6, args=[0])
    Clock.schedule(op_yr_iz.stop, Clock.now() + 8)
Clock.schedule(open_your_eyes, Clock.mod(8) - 1)

drums.hpf = 0

drums.hpf = var([0, 4000], [56, 8])

### Synths ###

build = Player()
ending_s = Player()

# build 1
def build_1():
    drums.amp = 0
    build >> loop("why_did_you_build1_120BPM.wav", P[:64], tempo=120)
Clock.schedule(build_1, Clock.mod(64) - 1)

# ending
def ending():
    drums.amp = 0
    ending_s >> loop("why_did_you_ending_120BPM.wav", P[:32], tempo=120)
Clock.schedule(build.stop, Clock.mod(8))
Clock.schedule(ending, Clock.mod(8) - 1)

# aux synth definitions
synth1 = Player()

synth1 >> ambi()

pl >> dbass([0, 0], dur=4, bpf=400, bpr=1).slider().spread()
