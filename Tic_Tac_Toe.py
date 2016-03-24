# -*- coding: utf-8 -*-
import Board
import NPC

#Atributos
t = Board.Board()
npc = NPC.NPC("O")

t.printTabuleiro()

#Loop do jogo
i = 0
while(i < 9):
    if i%2 != 0: #Vez da Maquina
        mark = "O"
        npc.play(t, mark)
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
    i += 1
if i == 9:
    print "Empate!"
