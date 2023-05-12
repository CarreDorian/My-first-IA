from Process_Neurones import *
from multiprocessing import Process, Queue

class Foret():
    def __init__(self, nbr_Neurones = 1, name = "poid"):
        self.arbres = []
        for i in range(nbr_Neurones):
            self.arbres.append(Neurones("csv/" + name + str(i+1)))
    
    def training(self, lst_users, repeat = 1):
        coeur = []
        for i in self.arbres:
            coeur.append(Process(target=i.training, args=(lst_users, repeat)))
            coeur[len(coeur)-1].start()
        for i in coeur[::-1]:
            i.join()
    
    def prediction(self, parrametre):
        self.action = 0
        self.horreur = 0
        self.policier = 0
        self.romantique = 0
        self.dessin_anime = 0
        self.profile = []

        coeur = []
        index = 0
        piles = []
        for i in self.arbres:
            piles.append(Queue())
            coeur.append(Process(target=i.prediction, args=(self, piles[index], parrametre)))
            coeur[index].start()
            index += 1
        for i in range(index):
            coeur[i].join()
            self.arbres[i].sortie = piles[i].get()
            self.arbres[i].profil_client = piles[i].get()

        len_proba_recup = [0,0,0,0,0]
        for i in self.arbres:
            if i.profil_client.action > 0.6 or i.profil_client.action < 0.4 :
                self.action += i.profil_client.action
                len_proba_recup[0] += 1
            if i.profil_client.horreur > 0.6 or i.profil_client.horreur < 0.4 :
                self.horreur += i.profil_client.horreur
                len_proba_recup[1] += 1
            if i.profil_client.policier > 0.6 or i.profil_client.policier < 0.4 :
                self.policier += i.profil_client.policier
                len_proba_recup[2] += 1
            if i.profil_client.romantique > 0.6 or i.profil_client.romantique < 0.4 :
                self.romantique += i.profil_client.romantique
                len_proba_recup[3] += 1
            if i.profil_client.dessin_anime > 0.6 or i.profil_client.dessin_anime < 0.4 :
                self.dessin_anime += i.profil_client.dessin_anime
                len_proba_recup[4] += 1
        self.action /= len_proba_recup[0]
        self.horreur /= len_proba_recup[1]
        self.policier /= len_proba_recup[2]
        self.romantique /= len_proba_recup[3]
        self.dessin_anime /= len_proba_recup[4]

        self.profil_client = profile("client", self.action, self.horreur, self.policier, self.romantique, self.dessin_anime, parrametre[0], parrametre[1], parrametre[2])
        self.profil_client.affich()

    def put(self, pile, sortie, profil_client):
        pile.put(sortie)
        pile.put(profil_client)