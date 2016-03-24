import Board

class NPC:

    #Metodo contrutor
    def __init__(self, mark):
        self.mark = mark

    # Tenta fazer a jogada em algum agente
    def tryPlay(self, tabuleiro, mark, pos1, pos2, pos3):
        if not tabuleiro.occupied(pos1):
            tabuleiro.setMark(pos1, mark)
        elif not tabuleiro.occupied(pos2):
            tabuleiro.setMark(pos2, mark)
        elif not tabuleiro.occupied(pos3):
            tabuleiro.setMark(pos3, mark)
        return tabuleiro
        

    #Acao de fazer a jogada
    def play(self, tabuleiro, mark):
        peso, agente = self.peso(tabuleiro, mark)
        if agente == "Linha 1":
            print "entrou na linha 1"
            self.tryPlay(tabuleiro, mark, 1, 2, 3)

        elif agente == "Linha 2":
            print "entrou na linha 2"
            self.tryPlay(tabuleiro, mark, 4, 5, 6)

        elif agente == "Linha 3":
            print "entrou na linha 3"
            self.tryPlay(tabuleiro, mark, 7, 8, 9)

        elif agente == "Coluna 1":
            print "entrou na coluna 1"
            self.tryPlay(tabuleiro, mark, 1, 4, 7)

        elif agente == "Coluna 2":
            print "entrou na coluna 2"
            self.tryPlay(tabuleiro, mark, 2, 5, 8)

        elif agente == "Coluna 3":
            print "entrou na coluna 3"
            self.tryPlay(tabuleiro, mark, 3, 6, 9)

        elif agente == "Diagonal 1":
            print "entrou na diagonal 1"
            self.tryPlay(tabuleiro, mark, 1, 5, 9)

        elif agente == "Diagonal 2":
            print "entrou na linha 2"
            self.tryPlay(tabuleiro, mark, 3, 5, 7) 
        else:
            print "jogou padrao"
            tabuleiro = self.defaultPlay( tabuleiro, mark )
        return tabuleiro
            
    def defaultPlay( self, tabuleiro, mark ):
        if not tabuleiro.occupied(5):
            tabuleiro.setMark(5, mark)
        elif not tabuleiro.occupied(1):
            tabuleiro.tab[0] = mark
        elif not tabuleiro.occupied(3):
            tabuleiro.tab[2] = mark
        elif not tabuleiro.occupied(7):
            tabuleiro.tab[6] = mark
        elif not tabuleiro.occupied(9):
            tabuleiro.tab[8] = mark
        elif not tabuleiro.occupied(2):
            tabuleiro.tab[1] = mark
        elif not tabuleiro.occupied(4):
            tabuleiro.tab[3] = mark
        elif not tabuleiro.occupied(6):
            tabuleiro.tab[5] = mark
        elif not tabuleiro.occupied(8):
            tabuleiro.tab[7] = mark
        else:
            print "Erro NPC"
        return tabuleiro


    # Se a posicao estiver vazia marca a nova posicao e retorna o tabuleiro,
    # Se nao retorna um tabuleiro vazio
    def marca(self, i, marca, tab):
        if tab[i] == " ":
            tab.setMark(i, marca)
            return tab
        else:
            return Tabuleiro.Tabuleiro()
        
    # Caso a posicao esteja livre.
    def free(self, tab, a, b, c):
        if tab.tab[a] != "X" and tab.tab[b] != "X" and tab.tab[c] != "X":
            return True
        else:
            return False
        
    # Retorna o o quantitativo de adaptacao do tabuleiro e o agente em que ira marcar
    def peso(self, tab, marca):
        if self.free(tab, 0, 1, 2) and(tab.tab[0] == tab.tab[1] == marca or
                                       tab.tab[1] == tab.tab[2] == marca or tab.tab[0] == tab.tab[2] == marca): #Linha 1
            return 2, "Linha 1"
        elif self.free(tab, 3, 4, 5) and (tab.tab[3] == tab.tab[4] == marca or
                                          tab.tab[4] == tab.tab[5] == marca or tab.tab[3] == tab.tab[5] == marca): #Linha 2
            return 2, "Linha 2"
        elif self.free(tab, 6, 7, 8) and (tab.tab[6] == tab.tab[7] == marca or
                                          tab.tab[7] == tab.tab[8] == marca or tab.tab[6] == tab.tab[8] == marca): #Linha 3
            return 2, "Linha 3"
        elif self.free(tab, 0, 3, 6) and (tab.tab[0] == tab.tab[3] == marca or
                                          tab.tab[3] == tab.tab[6] == marca or tab.tab[0] == tab.tab[6] == marca): #Coluna 1
            return 2, "Coluna 1"
        elif self.free(tab, 1, 4, 7) and (tab.tab[1] == tab.tab[4] == marca or
                                          tab.tab[4] == tab.tab[7] == marca or tab.tab[1] == tab.tab[7] == marca): #Coluna 2
            return 2, "Coluna 2"
        elif self.free(tab, 2, 5, 8) and (tab.tab[2] == tab.tab[5] == marca or
                                          tab.tab[5] == tab.tab[8] == marca or tab.tab[2] == tab.tab[8] == marca): #Coluna 3
            return 2, "Coluna 3"
        elif self.free(tab, 0, 4, 8) and (tab.tab[0] == tab.tab[4] == marca or
                                          tab.tab[4] == tab.tab[8] == marca or tab.tab[0] == tab.tab[8] == marca): #Diagonal 1
            return 2, "Diagonal 1"
        elif self.free(tab, 2, 4, 6) and (tab.tab[2] == tab.tab[4] == marca or
                                          tab.tab[4] == tab.tab[6] == marca or tab.tab[2] == tab.tab[6] == marca): #Diagonal 2
            return 2, "Diagonal 2"
        elif self.free(tab, 0, 1, 2) and (tab.tab[0] == marca or tab.tab[1] == marca or
                                          tab.tab[2] == marca): #Linha 1
            return 1, "Linha 1"
        elif self.free(tab, 3, 4, 5) and (tab.tab[3] == marca or tab.tab[4] == marca or
                                          tab.tab[5] == marca): #Linha 2
            return 1, "Linha 2"
        elif self.free(tab, 6, 7, 8) and (tab.tab[6] == marca or tab.tab[7] == marca or
                                          tab.tab[8] == marca): #Linha 3
            return 1, "Linha 3"
        elif self.free(tab, 0, 3, 6) and (tab.tab[0] == marca or tab.tab[3] == marca or
                                          tab.tab[6] == marca): #Coluna 1
            return 1, "Coluna 1"
        elif self.free(tab, 1, 4, 7) and (tab.tab[1] == marca or tab.tab[4] == marca or
                                          tab.tab[7] == marca): #Coluna 2
            return 1, "Coluna 2"
        elif self.free(tab, 2, 5, 8) and (tab.tab[2] == marca or tab.tab[5] == marca or
                                          tab.tab[8] == marca): #Coluna 3
            return 1, "Coluna 3"
        elif self.free(tab, 0, 4, 8) and (tab.tab[0] == marca or tab.tab[4] == marca or
                                          tab.tab[8] == marca): #Diagonal 1
            return 1, "Diagonal 1"
        elif self.free(tab, 2, 4, 6) and (tab.tab[2] == marca or tab.tab[4] == marca or
                                          tab.tab[6] == marca): #Diagonal 2 
            return 1, "Diagonal 2"
        else:
            return 0, ""
