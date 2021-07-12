from Process_Neurones import Neurones
from threading import Thread

class Threading(Neurones, Thread):
    def __init__(self, name, show_confidence = False):
        Neurones.__init__(self, name, show_confidence)
        Thread.__init__(self)
        self.parrametre = ""
        self.action = "no"
        self.train = 1
        self.start()
    
    def run(self):
        if self.action == "train":
            self.training(self.parrametre, self.train)
        elif self.action == "prediction":
            self.prediction(self.parrametre)
        else:
            pass

    def prediction(self, entree):
        try:
            for i in range (3):
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
