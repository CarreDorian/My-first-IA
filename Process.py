from Process_Neurones import *
from multiprocessing import Process, Queue

class Foret():
    def __init__(self, nbr_Neurones = 1, name = "poid", show_confidence = False):
        self.arbres = []
        self.show_confidence = show_confidence
        for i in range(nbr_Neurones):
            self.arbres.append(Neurones("csv/" + name + str(i+1), show_confidence))
    
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

        for i in self.arbres:
            self.action += i.profil_client.action
            self.horreur += i.profil_client.horreur
            self.policier += i.profil_client.policier
            self.romantique += i.profil_client.romantique
            self.dessin_anime += i.profil_client.dessin_anime
        self.action /= len(self.arbres)
        self.horreur /= len(self.arbres)
        self.policier /= len(self.arbres)
        self.romantique /= len(self.arbres)
        self.dessin_anime /= len(self.arbres)

        self.profil_client = profile("client", self.action, self.horreur, self.policier, self.romantique, self.dessin_anime, parrametre[0], parrametre[1], parrametre[2])
        self.profil_client.affich(self.show_confidence)

    def put(self, pile, sortie, profil_client):
        pile.put(sortie)
        pile.put(profil_client)