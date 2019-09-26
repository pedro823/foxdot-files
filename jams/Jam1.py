Scale.default = 'minor'
Root.default = -4
Clock.bpm = 120

var.bass_prog = var([0, 0, 0, 0, 2, 2, 1, 1], 2)

def grow(to, how_long=32, fr=0):
    return linvar([fr, to], [how_long, inf], start=now)

c1 >> dirt(var.bass_prog + [0, 0, 7, 0, 0, 7, 0, 6], amp=grow(0.7), dur=1/2, room=0.3).spread().stop()

c2 >> dbass(var.bass_prog, amp=0.4, dur=1, drive=0.03)

s3 >> pluck(var.bass_prog + [4, 5, 7, 4, 2, 0, 7, 0], dur=1/2, amp=grow(1)).stop()

s2 >> pasha(P[0, 4, 4, 0, 4, 0, 5, 0] + 14, dur=1/4, amp=0.2).stop()

s1 >> pads(var.bass_prog + [-1, 0, 2, 4], dur=4, spin=4, amp=1.2, chop=[8, 16], hpf=linvar([500, 2000], 16), hpr=0.2).every(8, 'shuffle').spread().stop()


d1 >> play('x ', amp=grow(1.2)).stop()

d3 >> play('<x---O---><|s1|       >', amp=grow(0.8), dur=[1/4, 1/2, 1/2, 3/4, 1/2, 1/2, 1/2, 1/2]).stop()

d2 >> play('       [ss]', sample = 2, amp=grow(0.8)).spread().stop()



ee >> bug([1, 2, 1], dur=8, amp=grow(0.3, how_long=16)).stop()

ss >> sinepad([0, 2, 4], dur=10, coarse=2, chop=0).stop()

#kkkkkkkkkkkkkk
pp >> play("vem de").stop()
zz >> zap([7, 6, 5], amp=0.2).stop()

bb >> sawbass().follow(c1).stop()

# TE AMO.
# tripletsssss ÉOQ <<<<<< TRIplets
# pra vc ver uia HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUM MOçA DO çEU
# >>>>>>>>>3<<<<<<<<<<<  notas em 1 beat == triplet
lk >> sawbass(var.bass_prog + [2, 1, 0], dur=2/3, coarse=1, chop=0).stop()
#PORRA ERA ISSO QUE EU QUERIAAAAAAAAA
#mas nao sabia faze

gi >> play("3! = 6  ", amp=0.6).stop()

# vamo fazer musica em 5/4? ata
# huashuhsuhau
# vou te mostrar

# COMPASSO DE MUSICA
# 4/4: o que a gente ta acostumado a ouvir, 4 notas num compasso
#uhum
pa >> play('x-x-').stop()
# 3/4: masoq tem 3 notas do mesmo tamanho que a anterior, mas so tem 3
# Forte fraco fraco
pb >> play('x--').stop()

# 5/4: Agora tem 5 espacos pra nota
# faz sentido?
# MDS PARECE DAFT PUNK - ROLLING n SCRATCHING
pc >> play('orrL').stop() #PQP EU AMO ESSE L eh mto bom PARECE LORde
# sabe o que vc pode fazer?
# combar ele com um kick
#O QUE SPREAD FAZ? dissoa o som entre os dois alto falantesPERCEBIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII#III
#MDS ISSO TQ LINDO
#noss isso ta quase LORDE

var.chords = var([0, 0, 0, -1], 6)
var.bass = var([[1, 2, 2, 2], 0, 0, 0], [1, 2, 2, 1])

pd >> play('<X  o  ><x  L ( s)>').spread()
#:o
s1 >> dbass(var.chords + var.bass, dur=[1, 2, 2, 1], lpf=300, lpr=0.3)

s2 >> dirt(var.chords + var.bass + 7, dur=[1, 2, 2, 1], hpf=linvar([4000, 200], 16))

d2 >> play('n N s ', dur=1/2, sample=PRand(4), pan=PWhite(-1, 1), rate=PRand(1, 5))

d3 >> saw([0, 5, 0, 0, 4, 0, 0, 4, 0], dur=1).spread().stop()

#deusme livre daft paft
# kkkkkkk
# gildo eh 5/4
# Pra vc deixar o gildo 4/4, vc tem que deixar a bateria em multiplos de 4

# 6/4 eh fantastico


# O numero que vem ANTES da barra eh a quantia de notas, o que vem DEPOIS e o tamanho da nota
# sim, os compassos podem ficar bem esquisitos
# 11/8 por exemplo
#sim entendi mas eh meio esquisito ne




#cade meu momolado A
#oie

#eu nao entendo vc pedro


mm >> play("--xo").stop()
# AH PRONTO
# <e

ld >> play("jesus cowboY ").stop()

oi >> play(" e").stop()