(
SynthDef(\whitenoise, {
	|freq = 440, amp = 0.3, sus = 1, pan = 0, t_gate = 0|
	var ampNow = EnvGen.kr(Env.new([0, 1, 0], [0.001, sus], \hold), doneAction: 2);
	Out.ar([0, 1],
		BPF.ar(
			WhiteNoise.ar(amp!2) * ampNow,
			freq
		)
	);
}).add;
)

(
x = Synth(\whitenoise, [\freq, 1000, \sus, 0.25])
)

FoxDot.start