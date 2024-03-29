import random
from os import mkdir

def split (element):
    element = element.split(",")
    to_return = []
    number = 0
    for i in element:
        is_neg = False

        if i[0] == '-':
            is_neg = True
            i = i[1:]

        i = i.split(".")
        if len(i) > 2:
            return "ERROR"
        
        try:
            number = float(i[0])
            number += float(i[1]) / (10 ** len(i[1]))
        except:
            return "ERROR"
        
        if is_neg:
            number *= -1
        
        to_return.append(number)

    return to_return

class Poids:
    def __init__ (self, name = "poids"):
        self.experience = 0
        self.Overflow_Error = 0
        try:
            self.file_name = name + ".csv"
            file = open(self.file_name, "r").read().split("\n")
            for i in file:
                self.csv_line(i)

        except:
            pass
        
        try:
            self.W1_poids
        except:
            self.W1_poids = [ 
                          [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                          [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                          [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                          [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001]
                        ]
        try:
            self.W2_poids
        except:
            self.W2_poids = [ 
                          [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                          [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                          [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001]
                        ]
        try:
            self.sortie_poids
        except:
            self.sortie_poids = [
                              [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                              [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                              [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                              [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001],
                              [random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001, random.randint(-500000, 500000) * 0.00001]
                            ]
        
        self.action = ""

    def csv_line (self, element):
        try:
            element = element.split(" ; ")
            if element[0] == "W1":
                W1 = []
                for i in element[1:]:
                    i = split(i)
                    if i == "ERROR":
                        return
                    W1.append(i)
                self.W1_poids = W1
            
            elif element[0] == "W2":
                W2 = []
                for i in element[1:]:
                    i = split(i)
                    if i == "ERROR":
                        return
                    W2.append(i)
                self.W2_poids = W2
            
            elif element[0] == "WF":
                WF = []
                for i in element[1:]:
                    i = split(i)
                    if i == "ERROR":
                        return
                    WF.append(i)
                self.sortie_poids = WF
            
            elif element[0] == "XP":
                int(element[2])
                self.experience = int(element[1])
                self.Overflow_Error = int(element[2])
        except:
            pass
    
    def affich (self):
        for i in self.W1_poids:
            W1_affich = ""
            for j in i:
                W1_affich += str(j) + " ; "

        for i in self.W2_poids:
            W2_affich = ""
            for j in i:
                W2_affich += str(j) + " ; "

        for i in self.sortie_poids:
            WF_affich = ""
            for j in i: 
                WF_affich += str(j) + " ; "

    def save(self):
        try:
            n = open(self.file_name, "w")
        except:
            mkdir("./csv")
            n = open(self.file_name, "w")

        W1_affich = ""
        for i in self.W1_poids:
            W1_affich += " ; "
            for j in i:
                W1_affich += str(j) + ","
            W1_affich = W1_affich[:len(W1_affich)-1]
                
        W2_affich = ""
        for i in self.W2_poids:
            W2_affich += " ; "
            for j in i:
                W2_affich += str(j) + ","
            W2_affich = W2_affich[:len(W2_affich)-1]
                
        WF_affich = ""
        for i in self.sortie_poids:
            WF_affich += " ; "
            for j in i:
                WF_affich += str(j) + ","
            WF_affich = WF_affich[:len(WF_affich)-1]

        n.write("Couche ; Neurone1 ; Neurone2 ; Neurone3 ; ...\nW1" + W1_affich + "\nW2" + W2_affich + "\nWF" + WF_affich + "\nXP ; " + str(self.experience) + " ; " + str(self.Overflow_Error))
        n.close()
