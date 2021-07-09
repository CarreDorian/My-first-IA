class profile:
    def __init__(self, name, action, horreur, policier, romantique, dessin_anime, age, bac, sexe):
        self.lst = [name, action, horreur, policier, romantique, dessin_anime, age, bac, sexe]
        self.action = action
        self.horreur = horreur
        self.policier = policier
        self.romantique = romantique
        self.dessin_anime = dessin_anime
        self.name = name
        self.age = age
        self.bac = bac
        self.sexe = sexe

    def film(self, test, element):
        if (test == 1):
            try:
                self.like += element + ", "
            except:
                if (self.sexe):
                    self.like = "Il aime "
                else:
                    self.like = "Elle aime "
                self.like += element + ", "
             
        elif (test == 0):
            try:
                self.dislike += element + ", "
            except:
                if (self.sexe):
                    self.dislike = "Il n'aime pas "
                else:
                    self.dislike = "Elle n'aime pas "
                self.dislike += element + ", "

        elif (test > 0.5):
            proba = (((round(test, 2) * 100) - 50) / 50) * 100
            try:
                self.like += element + " (" + str(proba) + " %), "
            except:
                if (self.sexe):
                    self.like = "Il aime "
                else:
                    self.like = "Elle aime "
                self.like += element + " (" + str(proba) + " %), "

        elif (test < 0.5):
            proba = ((50 - round(test, 2) * 100) / 50) * 100
            try:
                self.dislike += element + " (" + str(proba) + " %), "
            except:
                if (self.sexe):
                    self.dislike = "Il n'aime pas "
                else:
                    self.dislike = "Elle n'aime pas "
                self.dislike += element + " (" + str(proba) + " %), "

        else:
            print("Bad probability")

    def affich(self):
        if (self.bac == 1):
            bac = "possede le bac"
        elif (self.bac):
            bac = "possede un bac +" + str(self.bac - 1)
        else:
            bac = "ne possede pas de bac"
        
        self.film(self.action, "les films d'action")
        self.film(self.horreur, "les films d'horreur")
        self.film(self.policier, "les films policier")
        self.film(self.romantique, "les films romantique")
        self.film(self.dessin_anime, "les dessins animes")
        
        affich = self.name + " a " + str(self.age) + " ans, et " + bac + ".\n"
        try:
            self.like = self.like[:len(self.like)-2] + ". "
            affich += self.like + "\n"
        except:
            pass
        try:
            self.dislike = self.dislike[:len(self.dislike)-2] + ". "
            affich += self.dislike + "\n"
        except:
            pass
        print (affich)


    56
    100