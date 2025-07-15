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
        test = round((test - 0.5) * 200, 2)
        if (test == 100):
            try:
                self.like += element + ", "
            except:
                if (self.sexe):
                    self.like = "Il aime "
                else:
                    self.like = "Elle aime "
                self.like += element + ", "
             
        elif (test == -100):
            try:
                self.dislike += element + ", "
            except:
                if (self.sexe):
                    self.dislike = "Il n'aime pas "
                else:
                    self.dislike = "Elle n'aime pas "
                self.dislike += element + ", "

        elif (test > 10):
            try:
                self.like += element + " (" + str(test) + " %), "
            except:
                if (self.sexe):
                    self.like = "Il aime "
                else:
                    self.like = "Elle aime "
                self.like += element + " (" + str(test) + " %), "

        elif (test < -10):
            test = -test
            try:
                self.dislike += element + " (" + str(test) + " %), "
            except:
                if (self.sexe):
                    self.dislike = "Il n'aime pas "
                else:
                    self.dislike = "Elle n'aime pas "
                self.dislike += element + " (" + str(test) + " %), "

        else:
            try:
                self.neutral += element + " (" + str(test) + " %), "
            except:
                self.neutral = "Je ne sais pas pour " + element + " (" + str(test) + " %), "

    def affich(self):
        if self.bac > 0:
            bac = "possede l'occupation n°" + str(self.bac)
        else:
            bac = "ne possede pas d'activitée"
        if self.sexe == 1:
            sexe = "un homme"
        else:
            sexe = "une femme"
        
        self.film(self.action, "les films d'action")
        self.film(self.horreur, "les films d'horreur")
        self.film(self.policier, "les films policier")
        self.film(self.romantique, "les films romantique")
        self.film(self.dessin_anime, "les dessins animes")
        
        affich = self.name + " a " + str(self.age) + "ans, est " + sexe + ", et " + bac + ".\n"
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
        try:
            self.neutral = self.neutral[:len(self.neutral)-2] + ". "
            affich += self.neutral + "\n"
        except:
            pass
        print (affich)

