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

    def film_without_confidence(self, test, element):
        if (test > 0.5):
            try:
                self.like += element + ", "
            except:
                if (self.sexe):
                    self.like = "He like "
                else:
                    self.like = "She like "
                self.like += element + ", "

        elif (test <= 0.5):
            try:
                self.dislike += element + ", "
            except:
                if (self.sexe):
                    self.dislike = "He dislike "
                else:
                    self.dislike = "She dislike "
                self.dislike += element + ", "

        else:
            print("Bad probability")

    def film_with_confidence(self, test, element):
        if (test == 1):
            try:
                self.like += element + ", "
            except:
                if (self.sexe):
                    self.like = "He like "
                else:
                    self.like = "She like "
                self.like += element + ", "
             
        elif (test == 0):
            try:
                self.dislike += element + ", "
            except:
                if (self.sexe):
                    self.dislike = "He dislike "
                else:
                    self.dislike = "She dislike "
                self.dislike += element + ", "

        elif (test > 0.5):
            proba = (((round(test, 2) * 100) - 50) / 50) * 100
            try:
                self.like += element + " (" + str(round(proba, 2)) + " %), "
            except:
                if (self.sexe):
                    self.like = "He like "
                else:
                    self.like = "She like "
                self.like += element + ", " + " (" + str(round(proba, 2)) + " %), "

        elif (test <= 0.5):
            proba = ((50 - round(test, 2) * 100) / 50) * 100
            try:
                self.dislike += element + " (" + str(round(proba, 2)) + " %), "
            except:
                if (self.sexe):
                    self.dislike = "He dislike "
                else:
                    self.dislike = "She dislike "
                self.dislike += element + " (" + str(round(proba, 2)) + " %), "

        else:
            print("Bad probability")

    def affich(self, show_confidence = False):
        if (self.bac == 1):
            bac = "get a bac"
        elif (self.bac):
            bac = "get a bac +" + str(self.bac - 1)
        else:
            bac = "don't get a bac"
        
        if show_confidence:
            self.film_with_confidence(self.action, "the action film")
            self.film_with_confidence(self.horreur, "the horror film")
            self.film_with_confidence(self.policier, "the police film")
            self.film_with_confidence(self.romantique, "the romantic film")
            self.film_with_confidence(self.dessin_anime, "the cartoon film")
        else:
            self.film_without_confidence(self.action, "the action film")
            self.film_without_confidence(self.horreur, "the horror film")
            self.film_without_confidence(self.policier, "the police film")
            self.film_without_confidence(self.romantique, "the romantic film")
            self.film_without_confidence(self.dessin_anime, "the cartoon film")
        
        affich = self.name + " got " + str(self.age) + " years old, and " + bac + ".\n"
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

