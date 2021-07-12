from profile import profile
from Thread_Neurone import Threading
from profile import *

class Foret():
    def __init__(self, nbr_Neurones = 1, name = "poid", show_confidence = False):
        self.arbres = []
        for i in range(nbr_Neurones):
            self.arbres.append(Threading("csv/" + name + str(i+1), show_confidence))
    
    def training(self, lst_users, repeat = 1):
        for _ in range(repeat):
            for user in lst_users:
                for i in self.arbres:
                    i.parrametre = user.lst
                    i.action = "entrainement"
                    i.run()

            for i in self.arbres:
                i.join()
                i.save()
    
    def prediction(self, parrametre):
        self.action = 0
        self.horreur = 0
        self.policier = 0
        self.romantique = 0
        self.dessin_anime = 0
        self.profile = []
        for i in self.arbres:
            i.parrametre = parrametre
            i.action = "prediction"
            i.run()
        
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
        self.profil_client.affich()

    def put(self, pile, sortie, profil_client):
        pass