import math
from profile import profile
from Save import *

def sigmoid_derivee(x):
    return math.exp(-x) / (1+ math.exp(-x))**2

class Neurones(Poids):
    def __init__(self, name = "poids"):
        Poids.__init__(self, name)
        self.sortie = []
        self.profil_client = "coucou"

    def sigmoid (self, x):
        try:
            return 1/(1+math.exp(-x))
        except OverflowError:
            self.Overflow_Error += 1
            return 0

    def training(self, parrametres, repeat):
        # print(parrametre)
        for i in range(repeat):
            for parrametre in parrametres:
                parrametre = parrametre.lst
                try:
                    if (type(parrametre[0]) != str):
                        print("ENTREE_ERROR_")
                        return "ERROR";
                    for i in range (1, 6):
                        if 0 > parrametre[i]:
                            print("ENTREE_ERROR_1")
                            return "ERROR"
                    for i in range (1, 6):
                        if 1 < parrametre[i]:
                            print("ENTREE_ERROR_2")
                            return "ERROR"
                    if 1 < parrametre[8]:
                        print("ENTREE_ERROR_3")
                        return "ERROR"
                except:
                    print("ENTREE_ERROR_4")
                    return "ERROR"

                result = parrametre[1:6]
                entree = parrametre[6:]

                self.forword(entree)
                self.backword(entree, result, self.sortie)
        self.save()

    def prediction(self, parent, pile, entree):
        try:
            for i in range(3):
                if 0 > entree[i]:
                    print("ERROR")
                    return 
            if (entree[2] < 0) or (entree[2] > 1):
                print("ERROR")
                return
        except:
            print("ENTREE_ERROR")
            return
    
        self.forword(entree)
        parent.put(pile, self.sortie, self.profil_client)

    def forword(self, entree_matrice):
        self.W1 = [ 
                    entree_matrice[0] * self.W1_poids[0][0] + entree_matrice[1] * self.W1_poids[0][1] + entree_matrice[2] * self.W1_poids[0][2],
                    entree_matrice[0] * self.W1_poids[1][0] + entree_matrice[1] * self.W1_poids[1][1] + entree_matrice[2] * self.W1_poids[1][2],
                    entree_matrice[0] * self.W1_poids[2][0] + entree_matrice[1] * self.W1_poids[2][1] + entree_matrice[2] * self.W1_poids[2][2],
                    entree_matrice[0] * self.W1_poids[3][0] + entree_matrice[1] * self.W1_poids[3][1] + entree_matrice[2] * self.W1_poids[3][2]
                  ]
        self.W1 = [ self.sigmoid(self.W1[0]), self.sigmoid(self.W1[1]), self.sigmoid(self.W1[2]), self.sigmoid(self.W1[3]) ]
        
        self.W2 = [ 
                    self.W1[0] * self.W2_poids[0][0] + self.W1[1] * self.W2_poids[0][1] + self.W1[2] * self.W2_poids[0][2] + self.W1[3] * self.W2_poids[0][3],
                    self.W1[0] * self.W2_poids[1][0] + self.W1[1] * self.W2_poids[1][1] + self.W1[2] * self.W2_poids[1][2] + self.W1[3] * self.W2_poids[1][3],
                    self.W1[0] * self.W2_poids[2][0] + self.W1[1] * self.W2_poids[2][1] + self.W1[2] * self.W2_poids[2][2] + self.W1[3] * self.W2_poids[2][3]
                  ]
        self.W2 = [ self.sigmoid(self.W2[0]), self.sigmoid(self.W2[1]), self.sigmoid(self.W2[2]) ]     
        
        self.sortie = [ self.W2[0] * self.sortie_poids[0][0] + self.W2[1] * self.sortie_poids[0][1] + self.W2[2] * self.sortie_poids[0][2],
                    self.W2[0] * self.sortie_poids[1][0] + self.W2[1] * self.sortie_poids[1][1] + self.W2[2] * self.sortie_poids[1][2],
                    self.W2[0] * self.sortie_poids[2][0] + self.W2[1] * self.sortie_poids[2][1] + self.W2[2] * self.sortie_poids[2][2],
                    self.W2[0] * self.sortie_poids[3][0] + self.W2[1] * self.sortie_poids[3][1] + self.W2[2] * self.sortie_poids[3][2],
                    self.W2[0] * self.sortie_poids[4][0] + self.W2[1] * self.sortie_poids[4][1] + self.W2[2] * self.sortie_poids[4][2]
                  ]
        self.sortie = [ self.sigmoid(self.sortie[0]), self.sigmoid(self.sortie[1]), self.sigmoid(self.sortie[2]), self.sigmoid(self.sortie[3]), self.sigmoid(self.sortie[4]) ]

        self.profil_client = profile("client", self.sortie[0], self.sortie[1], self.sortie[2], self.sortie[3], self.sortie[4], entree_matrice[0], entree_matrice[1], entree_matrice[2])

    def backword(self, entree_matrice, WF_attendu, WF):
        erreur = [ 
                    WF_attendu[0] - WF[0],
                    WF_attendu[1] - WF[1],
                    WF_attendu[2] - WF[2],
                    WF_attendu[3] - WF[3],
                    WF_attendu[4] - WF[4]
                 ]
        erreur_delta = [ 
                    erreur[0] * sigmoid_derivee(WF[0]),
                    erreur[1] * sigmoid_derivee(WF[1]),
                    erreur[2] * sigmoid_derivee(WF[2]),
                    erreur[3] * sigmoid_derivee(WF[3]),
                    erreur[4] * sigmoid_derivee(WF[4])
                 ]
        erreur_W2 = [
                        erreur_delta[0] * self.sortie_poids[0][0] + erreur_delta[1] * self.sortie_poids[1][0] + erreur_delta[2] * self.sortie_poids[2][0] + erreur_delta[3] * self.sortie_poids[3][0] + erreur_delta[4] * self.sortie_poids[4][0],
                        erreur_delta[0] * self.sortie_poids[0][1] + erreur_delta[1] * self.sortie_poids[1][1] + erreur_delta[2] * self.sortie_poids[2][1] + erreur_delta[3] * self.sortie_poids[3][1] + erreur_delta[4] * self.sortie_poids[4][1],
                        erreur_delta[0] * self.sortie_poids[0][2] + erreur_delta[1] * self.sortie_poids[1][2] + erreur_delta[2] * self.sortie_poids[2][2] + erreur_delta[3] * self.sortie_poids[3][2] + erreur_delta[4] * self.sortie_poids[4][2]
                    ]
        erreur_delta_W2 = [
                    erreur_W2[0] * self.sigmoid(self.W2[0]),
                    erreur_W2[1] * self.sigmoid(self.W2[1]),
                    erreur_W2[2] * self.sigmoid(self.W2[2])
        ]
        erreur_W1 = [
                    erreur_delta_W2[0] * self.W2_poids[0][0] + erreur_delta_W2[1] * self.W2_poids[1][0] + erreur_delta_W2[2] * self.W2_poids[2][0],
                    erreur_delta_W2[0] * self.W2_poids[0][1] + erreur_delta_W2[1] * self.W2_poids[1][1] + erreur_delta_W2[2] * self.W2_poids[2][1],
                    erreur_delta_W2[0] * self.W2_poids[0][2] + erreur_delta_W2[1] * self.W2_poids[1][2] + erreur_delta_W2[2] * self.W2_poids[2][2],
                    erreur_delta_W2[0] * self.W2_poids[0][3] + erreur_delta_W2[1] * self.W2_poids[1][3] + erreur_delta_W2[2] * self.W2_poids[2][3]
        ]
        erreur_delta_W1 = [
                    erreur_W1[0] * self.sigmoid(self.W1[0]),
                    erreur_W1[1] * self.sigmoid(self.W1[1]),
                    erreur_W1[2] * self.sigmoid(self.W1[2]),
                    erreur_W1[3] * self.sigmoid(self.W1[3])
        ]
        
        self.W1_poids = [
                    [ self.W1_poids[0][0] + entree_matrice[0] * erreur_delta_W1[0], self.W1_poids[0][1] + entree_matrice[1] * erreur_delta_W1[0], self.W1_poids[0][2] + entree_matrice[2] * erreur_delta_W1[0] ],
                    [ self.W1_poids[1][0] + entree_matrice[0] * erreur_delta_W1[1], self.W1_poids[1][1] + entree_matrice[1] * erreur_delta_W1[1], self.W1_poids[1][2] + entree_matrice[2] * erreur_delta_W1[1] ],
                    [ self.W1_poids[2][0] + entree_matrice[0] * erreur_delta_W1[2], self.W1_poids[2][1] + entree_matrice[1] * erreur_delta_W1[2], self.W1_poids[2][2] + entree_matrice[2] * erreur_delta_W1[2] ],
                    [ self.W1_poids[3][0] + entree_matrice[0] * erreur_delta_W1[3], self.W1_poids[3][1] + entree_matrice[1] * erreur_delta_W1[3], self.W1_poids[3][2] + entree_matrice[2] * erreur_delta_W1[3] ]
        ]
        self.W2_poids = [
                    [ self.W2_poids[0][0] + self.W1[0] * erreur_delta_W2[0], self.W2_poids[0][1] + self.W1[1] * erreur_delta_W2[0], self.W2_poids[0][2] + self.W1[2] * erreur_delta_W2[0], self.W2_poids[0][3] + self.W1[3] * erreur_delta_W2[0] ],
                    [ self.W2_poids[1][0] + self.W1[0] * erreur_delta_W2[1], self.W2_poids[1][1] + self.W1[1] * erreur_delta_W2[1], self.W2_poids[1][2] + self.W1[2] * erreur_delta_W2[1], self.W2_poids[1][3] + self.W1[3] * erreur_delta_W2[1] ],
                    [ self.W2_poids[2][0] + self.W1[0] * erreur_delta_W2[2], self.W2_poids[2][1] + self.W1[1] * erreur_delta_W2[2], self.W2_poids[2][2] + self.W1[2] * erreur_delta_W2[2], self.W2_poids[2][3] + self.W1[3] * erreur_delta_W2[2] ]
        ]
        self.sortie_poids = [
                    [ self.sortie_poids[0][0] + self.W2[0] * erreur_delta[0], self.sortie_poids[0][1] + self.W2[1] * erreur_delta[0], self.sortie_poids[0][2] + self.W2[2] * erreur_delta[0] ],
                    [ self.sortie_poids[1][0] + self.W2[0] * erreur_delta[1], self.sortie_poids[1][1] + self.W2[1] * erreur_delta[1], self.sortie_poids[1][2] + self.W2[2] * erreur_delta[1] ],
                    [ self.sortie_poids[2][0] + self.W2[0] * erreur_delta[2], self.sortie_poids[2][1] + self.W2[1] * erreur_delta[2], self.sortie_poids[2][2] + self.W2[2] * erreur_delta[2] ],
                    [ self.sortie_poids[3][0] + self.W2[0] * erreur_delta[2], self.sortie_poids[3][1] + self.W2[1] * erreur_delta[2], self.sortie_poids[3][2] + self.W2[2] * erreur_delta[2] ],
                    [ self.sortie_poids[4][0] + self.W2[0] * erreur_delta[2], self.sortie_poids[4][1] + self.W2[1] * erreur_delta[2], self.sortie_poids[4][2] + self.W2[2] * erreur_delta[2] ]
        ]
        
        self.experience += 1