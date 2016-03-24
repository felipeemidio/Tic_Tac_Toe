# -*- coding: utf-8 -*-
#Classe que representa um tabuleiro de Jogo da velha
class Board():
    #Construtor
    def __init__(self):
        #A tabela é representada por uma array de espaços
        self.tab = [] 
        for i in range(10):
            self.tab.append(" ")

    #imprime a tabela na linha de comando
    def printTabuleiro(self):
        print "%s|%s|%s" % (self.tab[0], self.tab[1], self.tab[2])
        print "------"
        print "%s|%s|%s" % (self.tab[3], self.tab[4], self.tab[5])
        print "------"
        print "%s|%s|%s" % (self.tab[6], self.tab[7], self.tab[8])

    #Retorna se a posicao no tabuleiro esta ocupada ou nao
    def occupied(self, position):
        if self.tab[position-1] == " ":
            return False
        else:
            return True

    #Funcao set das casas do tabuleiro
    def setMark(self, position, mark):
        if position < 1 or position > 9 :
            print "posicao fora dos limites"
            return False
        else:
            self.tab[position-1] = mark
            return True

    #Verifica se alguma condicao de vitoria foi feita
    def Win(self, mark):
        if self.tab[0] == self.tab[1] == self.tab[2] == mark:
            return True
        elif self.tab[3] == self.tab[4] == self.tab[5] == mark:
            return True
        elif self.tab[6] == self.tab[7] == self.tab[8] == mark:
            return True
        elif self.tab[0] == self.tab[3] == self.tab[6] == mark:
            return True
        elif self.tab[1] == self.tab[4] == self.tab[7] == mark:
            return True
        elif self.tab[2] == self.tab[5] == self.tab[8] == mark:
            return True
        elif self.tab[0] == self.tab[4] == self.tab[8] == mark:
            return True
        elif self.tab[2] == self.tab[4] == self.tab[6] == mark:
            return True
        else:
            return False
