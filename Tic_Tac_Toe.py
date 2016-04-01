# -*- coding: utf-8 -*-
import Board
import NPC

#Atributos
t = Board.Board()
npc = NPC.NPC("O")


#Escolhendo quem ira fazer o primeiro movimento
whoFirst = raw_input("Você quer jogar primeiro? [s/n]")
while True:
    if whoFirst == "s":
        rounds = 0
        break
    elif whoFirst == "n":
        rounds = 1
        break
    print "digite 's' ou 'n'"
    whoFirst = raw_input("Você quer jogar primeiro? [s/n]")

if rounds == 0:
    t.printTabuleiro()

#Loop do jogo
for i in range(rounds, rounds +10):
    if i%2 != 0: #Vez da Maquina
        mark = "O"
        npc.play(t)
        t.printTabuleiro()
        
    else: #Vez do Jogador
        mark = "X"
        move = input("Escolha a sua jogada\n")
        if t.occupied(move):  
            print "Movimento não aceito\nRepita sua jogada."
            i = i - 1
        else:
            t.setMark(move, mark)

    if t.Win(mark): #Alguem venceu?
        if mark == "X":
            print "Você venceu! Parabéns!"
        else: 
            print "Você perdeu, Vai tentar de novo?"
        break
if i == 9:
    print "Empate!"
