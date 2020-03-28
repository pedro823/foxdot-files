
# eu n sei oq eu to fazendo, mas eu voltei

# O DISCORD N CONECTA VAMO FALAR POR AQUI LOL RS

# OK 
# 1. As tres settings que importam -- BPM, escala e tom
Clock.bpm = 128 # BPM  # kkkkkk chaos
Root.default = 3 # A primeira nota
Scale.default = 'minor' # escala menor 

#danke

# vcs tao ai? sim
# o
#ye tosKKKKKKKKKKKKKKKKKK 

# 2. OK, vamo add uma batida

k1 >> play('<x ><X >', amp=1.3) # tum tum tum com low pass kkk

# se vc quiser ver quais samples tem,
print(Samples)

# vamo adicionar um clap
k2 >> play('  - ', bpf=700) # adicionei um filtro pra deixar menos agressivo o click

# e um shaker logo antes do clap?
k3 >> play('     ss ').stop()

r2 >> play('cN  ', bpf=sinvar([0, 2000], 8)) # o primeiro numero 
# eu n sei se r existe kkkkkkkkkkkkkkkkkkKKKKKKKKKK, eh r de ear Rape mds kkkkkkkk
# NEM BORREI AS CALCA N KKKKKKKKKKKKKKKKKKK 

# cara eu ainda to scrllando na wiki kkkk)

# Eu vou fazer o bass
var.bass = var([-10, -9, -8, -7], [3/2, 11/2, 5/2, 13/2])
bc >> bass(var.bass, lpf=sinvar([200, 8000], 64), dur=1/2, blur=1.3, amp=1)

var.synth1 = P[7, 0, 1, 2, -7, 2, 1, 0]
s1 >> pluck(var.synth1, dur=1/4, lpf=900, amp=1.8)

s2 >> orient(var(-14) + [6, 2, 2, 5, 4, 2, 5, 4], dur=[4, 4, 3/2, 1/2, 2, 3/2, 1/2, 2], lpf=800, room=0.4, mix=0.8).stop()

var.upper_synth_notes = list(map(lambda x: x+7, [-1, 4, 0, 3] * 4 + [-1, 4, 0, 3, 0, -1, 4, 0, 3]))
var.upper_synth_timing = [1/2, 1, 1/2, 1] * 2 + \
                         [1/2, 1/2, 1/2, 1/2] + \
                         [1/2, 1, 1/2, 1] + [1/2, 1, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2]

###

# Psum(m, n) tenta enfiar a quantidade m de notas em n beats
print(PSum(4, 2)) # check it out

# won't work, precisa ser numero
# isso 
p1 >> pluck([1, 3, 5, 8], dur=PSum(3, 2)).penta()

# dont do that
# essa budega NAO FUNCIONA em frequencias
# e sim em degraus dentro da escala
# tipo, 0 eh a primeira nota na escala, 1 eh a segunda, etc.
# ou seja, se vc trocar a escala, tudo ainda funciona, check it out
#A, B, C, D, E, F, G = 220, 246, 261, 294, 330, 349, 392


# mds
# instrumento cursed
# PNEU DE CARRO KKKKKKK teos
# eu n resisti
c2 >> pasha([1, 3, 5, 8], dur=PSum(3, 2), chop=4).penta()
# KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK

c3 >> pasha(var.bass + (0, 2, 4, 6, 9), dur=1/2)
# tem como deixar algo pregressivamente mais rapido?
# linvar, sinvar, expvar  
# tenta usar dur=expvar([4, 1/2], 16)


b2 >> sawbass([0,12], dur=)

print(expvar([0.1, 1/2], 16))


# 1.1.1.1 1 1 1 1 1 1  KKKK INTRO DE FUNK
# n funcionou? acho que n duracao eh em quantidade de batida, 1 eh a cada kick
p1 >> play("1   2   3   4   ").stop()

p1 >> pluck(oct=[3, 4, 5, 6])


