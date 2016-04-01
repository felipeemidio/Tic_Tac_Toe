import Board

class NPC:

    #Metodo contrutor
    def __init__(self, mark):
        self.mark = mark
        if mark == "O":
            self.oponent_mark = "X"
        elif mark == "X":
            self.oponent_mark = "O"

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
    #Analisa quem tem o maior 'peso' em fazer linhas
    #Se o jogador tiver maior peso que o npc, a jogada sera defensiva
    #Caso contrario sera ofensiva
    def play(self, tabuleiro):
        weight_npc, agent_npc = self.peso(tabuleiro, self.mark)
        weight_player, agent_player = self.peso(tabuleiro, "X")
        print weight_player, weight_npc
        if weight_player > weight_npc:
            if agent_player == "Linha 1":
                print "entrou na linha 1 player"
                self.tryPlay(tabuleiro, self.mark, 1, 2, 3)

            elif agent_player == "Linha 2":
                print "entrou na linha 2 player"
                self.tryPlay(tabuleiro, self.mark, 4, 5, 6)

            elif agent_player == "Linha 3":
                print "entrou na linha 3 player"
                self.tryPlay(tabuleiro, self.mark, 7, 8, 9)

            elif agent_player == "Coluna 1":
                print "entrou na coluna 1 player"
                self.tryPlay(tabuleiro, self.mark, 1, 4, 7)

            elif agent_player == "Coluna 2":
                print "entrou na coluna 2 player"
                self.tryPlay(tabuleiro, self.mark, 2, 5, 8)

            elif agent_player == "Coluna 3":
                print "entrou na coluna 3 player"
                self.tryPlay(tabuleiro, self.mark, 3, 6, 9)

            elif agent_player == "Diagonal 1":
                print "entrou na diagonal 1 player"
                self.tryPlay(tabuleiro, self.mark, 1, 5, 9)

            elif agent_player == "Diagonal 2":
                print "entrou na linha 2 player"
                self.tryPlay(tabuleiro, self.mark, 3, 5, 7) 
        else:
            if agent_npc == "Linha 1":
                print "entrou na linha 1"
                self.tryPlay(tabuleiro, self.mark, 1, 2, 3)

            elif agent_npc == "Linha 2":
                print "entrou na linha 2"
                self.tryPlay(tabuleiro, self.mark, 4, 5, 6)

            elif agent_npc == "Linha 3":
                print "entrou na linha 3"
                self.tryPlay(tabuleiro, self.mark, 7, 8, 9)

            elif agent_npc == "Coluna 1":
                print "entrou na coluna 1"
                self.tryPlay(tabuleiro, self.mark, 1, 4, 7)

            elif agent_npc == "Coluna 2":
                print "entrou na coluna 2"
                self.tryPlay(tabuleiro, self.mark, 2, 5, 8)

            elif agent_npc == "Coluna 3":
                print "entrou na coluna 3"
                self.tryPlay(tabuleiro, self.mark, 3, 6, 9)

            elif agent_npc == "Diagonal 1":
                print "entrou na diagonal 1"
                self.tryPlay(tabuleiro, self.mark, 1, 5, 9)

            elif agent_npc == "Diagonal 2":
                print "entrou na linha 2"
                self.tryPlay(tabuleiro, self.mark, 3, 5, 7) 
            else:
                print "jogou padrao"
                tabuleiro = self.defaultPlay( tabuleiro )

        return tabuleiro

    # Acao padrao caso nao haja melhor jogada          
    def defaultPlay( self, tabuleiro):
        if not tabuleiro.occupied(5):
            tabuleiro.setMark(5, self.mark)
        elif not tabuleiro.occupied(1):
            tabuleiro.tab[0] = self.mark
        elif not tabuleiro.occupied(3):
            tabuleiro.tab[2] = self.mark
        elif not tabuleiro.occupied(7):
            tabuleiro.tab[6] = self.mark
        elif not tabuleiro.occupied(9):
            tabuleiro.tab[8] = self.mark
        elif not tabuleiro.occupied(2):
            tabuleiro.tab[1] = self.mark
        elif not tabuleiro.occupied(4):
            tabuleiro.tab[3] = self.mark
        elif not tabuleiro.occupied(6):
            tabuleiro.tab[5] = self.mark
        elif not tabuleiro.occupied(8):
            tabuleiro.tab[7] = self.mark
        else:
            print "Erro NPC"
        return tabuleiro


    # Se a posicao estiver vazia marca a nova posicao e retorna o tabuleiro,
    # Se nao retorna um tabuleiro vazio
    def marca(self, i, tab):
        if tab[i] == " ":
            tab.setMark(i, self.mark)
            return tab
        else:
            return Tabuleiro.Tabuleiro()
        
    # Caso a posicao esteja livre.
    def free(self, tab, a, b, c, mark):
        opponentMark = "X"
        if mark == "X":
            opponentMark = "O"
        #else :
        #    oppenentMark = "X"
            
        if (tab.tab[a] != opponentMark and
            tab.tab[b] != opponentMark and tab.tab[c] != opponentMark):
            return True
        else:
            return False
        
    # Retorna o o quantitativo de adaptacao do tabuleiro e o agente em que ira marcar
    def peso(self, tab, mark):
        if self.free(tab, 0, 1, 2, mark) and(tab.tab[0] == tab.tab[1] == mark or
                                       tab.tab[1] == tab.tab[2] == mark or tab.tab[0] == tab.tab[2] == mark): #Linha 1
            return 2, "Linha 1"
        elif self.free(tab, 3, 4, 5, mark) and (tab.tab[3] == tab.tab[4] == mark or
                                          tab.tab[4] == tab.tab[5] == mark or tab.tab[3] == tab.tab[5] == mark): #Linha 2
            return 2, "Linha 2"
        elif self.free(tab, 6, 7, 8, mark) and (tab.tab[6] == tab.tab[7] == mark or
                                          tab.tab[7] == tab.tab[8] == mark or tab.tab[6] == tab.tab[8] == mark): #Linha 3
            return 2, "Linha 3"
        elif self.free(tab, 0, 3, 6, mark) and (tab.tab[0] == tab.tab[3] == mark or
                                          tab.tab[3] == tab.tab[6] == mark or tab.tab[0] == tab.tab[6] == mark): #Coluna 1
            return 2, "Coluna 1"
        elif self.free(tab, 1, 4, 7, mark) and (tab.tab[1] == tab.tab[4] == mark or
                                          tab.tab[4] == tab.tab[7] == mark or tab.tab[1] == tab.tab[7] == mark): #Coluna 2
            return 2, "Coluna 2"
        elif self.free(tab, 2, 5, 8, mark) and (tab.tab[2] == tab.tab[5] == mark or
                                          tab.tab[5] == tab.tab[8] == mark or tab.tab[2] == tab.tab[8] == mark): #Coluna 3
            return 2, "Coluna 3"
        elif self.free(tab, 0, 4, 8, mark) and (tab.tab[0] == tab.tab[4] == mark or
                                          tab.tab[4] == tab.tab[8] == mark or tab.tab[0] == tab.tab[8] == mark): #Diagonal 1
            return 2, "Diagonal 1"
        elif self.free(tab, 2, 4, 6, mark) and (tab.tab[2] == tab.tab[4] == mark or
                                          tab.tab[4] == tab.tab[6] == mark or tab.tab[2] == tab.tab[6] == mark): #Diagonal 2
            return 2, "Diagonal 2"
        elif self.free(tab, 0, 1, 2, mark) and (tab.tab[0] == mark or tab.tab[1] == mark or
                                          tab.tab[2] == mark): #Linha 1
            return 1, "Linha 1"
        elif self.free(tab, 3, 4, 5, mark) and (tab.tab[3] == mark or tab.tab[4] == mark or
                                          tab.tab[5] == mark): #Linha 2
            return 1, "Linha 2"
        elif self.free(tab, 6, 7, 8, mark) and (tab.tab[6] == mark or tab.tab[7] == mark or
                                          tab.tab[8] == mark): #Linha 3
            return 1, "Linha 3"
        elif self.free(tab, 0, 3, 6, mark) and (tab.tab[0] == mark or tab.tab[3] == mark or
                                          tab.tab[6] == mark): #Coluna 1
            return 1, "Coluna 1"
        elif self.free(tab, 1, 4, 7, mark) and (tab.tab[1] == mark or tab.tab[4] == mark or
                                          tab.tab[7] == mark): #Coluna 2
            return 1, "Coluna 2"
        elif self.free(tab, 2, 5, 8, mark) and (tab.tab[2] == mark or tab.tab[5] == mark or
                                          tab.tab[8] == mark): #Coluna 3
            return 1, "Coluna 3"
        elif self.free(tab, 0, 4, 8, mark) and (tab.tab[0] == mark or tab.tab[4] == mark or
                                          tab.tab[8] == mark): #Diagonal 1
            return 1, "Diagonal 1"
        elif self.free(tab, 2, 4, 6, mark) and (tab.tab[2] == mark or tab.tab[4] == mark or
                                          tab.tab[6] == mark): #Diagonal 2 
            return 1, "Diagonal 2"
        else:
            return 0, ""
