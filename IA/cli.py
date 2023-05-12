from sys import argv
from random import randint
from profile import profile
import Process, Thread
import pandas as pd

def init(famille, data):
    index_famille = 0
    index_membre = 0
    for index in data.index:
        index_membre += 1
        fam = famille[index_famille]
        if index_membre >= len(fam):
            index_membre = 1
            index_famille += 1
        if index_famille >= len(famille):
            index_famille = 0
            fam = famille[index_famille]

        membre = fam[index_membre]
        try:
            USERS.append( profile( membre[0] + " " + fam[0], int(data.action.values[index]), int(data.horreur.values[index]), int(data.policier.values[index]), int(data.romantique.values[index]), int(data.dessin_anime.values[index]), int(data.age.values[index]), int(data.bac.values[index]), int(data.sexe.values[index])) )
        except:
            print(membre[0] + " " + fam[0])
 
    # for j in famille:
    #     for i in j[1:]:
    #         try:
    #             USERS.append( profile( i[0] + " " + j[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]) )
    #         except:
    #             print(j[0] + ' ' + i[0])

doc_name = "cli.py"
def help():
    print("-------------------------------------------- help --------------------------------------------")
    print("")
    print("python " + doc_name + " : show the prediction of a profile and the reality")
    print("")
    print("Options :")
    print("-p, -process int : change the default number of heart use (6 by default)")
    print("-t, -thread int : use the threading module and no more the processing module. Nbr optionnal")
    print("-n, -name name : change the name of the csv file name")
    print("-T, -train int : make the training 'int' times")
    print("-h, -help : show this message and stop the programm")

def training(lst_users, to_predict):
    global ia, population, name, train
    if ia == "process":
        Einstein = Process.Foret(population, name)
    else:
        Einstein = Thread.Foret(population, name)

    Einstein.training(lst_users, train)
    print("The prediction is :")
    Einstein.prediction(to_predict)

def parcing():
    global argv_count
    global population 
    global ia
    if argv[argv_count][0] == "-":
        if argv[argv_count][1:] == "process" or argv[argv_count][1:] == "p":
            try:
                population = int(argv[argv_count + 1])
                argv_count += 1
            except:
                pass
            ia = "process"

        elif argv[argv_count][1:] == "thread" or argv[argv_count][1:] == "t":
            try:
                population = int(argv[argv_count + 1])
                argv_count += 1
            except:
                pass
            ia = "thread"

        elif argv[argv_count][1:] == "name" or argv[argv_count][1:] == "n":
            argv_count += 1
            global name
            name = argv[argv_count]

        elif argv[argv_count][1:] == "train" or argv[argv_count][1:] == "T":
            global train
            try:
                train = int(argv[argv_count + 1])
                argv_count += 1
            except:
                pass

        elif argv[argv_count][1:] == "help" or argv[argv_count][1:] == "h":
            help()
            return 1
    
USERS = []
ia = "process"
population = 6
argv_count = 1
name = "poid"
train = 0


if __name__ == "__main__": # "Entree" est utile pour donner des noms aux personnes annonymes et rendre les données plus humaines.
    Entree = [
        [ "puce", ["Bernard", 1, 1, 1, 0, 1, 80, 0, 1], ["Bernadette", 0, 0, 1, 1, 1, 81, 0, 0],
                        ["Jack", 1, 1, 1, 0, 0, 40, 0, 1], ["Tulipe", 0, 1, 0, 1, 1, 43, 0, 0],
                            ["Jean", 1, 1, 0, 0, 0, 20, 3, 1], ["Julie", 1, 0, 0, 1, 1, 25, 0, 0], ["Susane", 1, 1, 1, 0, 1, 23, 6, 0] ],
        
        [ "fleure", ["jaqueline", 0, 0, 1, 1, 1, 80, 6, 0], 
                        ["Jacob", 1, 1, 1, 0, 0, 48, 6, 1], ["Tulipette", 1, 0, 0, 1, 1, 55, 6, 0],
                            ["paul", 1, 1, 1, 0, 0, 15, 0, 1], ["Sogna", 1, 0, 0, 1, 1, 8, 0, 0], ["Morgane", 0, 0, 0, 0, 1, 4, 0, 0] ],

        [ "radiateur", ["Phillipe", 0, 0, 1, 0, 1, 80, 0, 1], ["Antoinette", 0, 0, 1, 0, 1, 85, 0, 0], ["Franck", 1, 0, 1, 0, 0, 75, 1, 1], ["Josianne", 1, 0, 1, 1, 1, 80, 1, 0],
                        ["Paul", 0, 0, 0, 1, 1, 30, 4, 0], ["Alice", 1, 1, 1, 1, 1, 24, 3, 0], ["Lionnel", 1, 1, 1, 0, 0, 35, 6, 0],
                            ["suson", 0, 1, 1, 0, 1, 8, 0, 0], ["Martine", 1, 0, 0, 1, 1, 20, 2, 0], ["Susette", 0, 1, 1, 0, 0, 25, 6, 0] ],
        
        [ "carbonne", ["Francois", 1, 0, 1, 0, 1, 95, 0, 1], ["lucette", 1, 0, 1, 0, 1, 89, 0, 0],
                        ["Claudine", 1, 1, 1, 1, 1, 45, 1, 0],
                            ["Sebastien", 1, 1, 0, 0, 0, 20, 3, 1], ["Laurent", 1, 1, 1, 0, 1, 14, 0, 1], ["Matilde", 1, 1, 0, 0, 1, 20, 3, 0], ["Pascale", 1, 1, 0, 0, 0, 28, 1, 1], ["Morgane", 1, 1, 0, 0, 1, 18, 1, 0] ],

        [ "boulet", # grands parents et Enfants abs
                        ["Fabien", 0, 0, 1, 1, 1, 40, 1, 1], ["Didier", 0, 0, 1, 1, 0, 45, 3, 1] ],
        
        [ "sucette", # grands parents abs
                        ["George", 0, 0, 1, 1, 0, 38, 4, 1], ["Celine", 1, 0, 1, 0, 1, 45, 6, 0],
                            ["Odile", 0, 0, 0, 0, 1, 12, 0, 0]  ],

        [ "bristol", # grands parents abs
                        ["Gaetan", 1, 1, 1, 0, 1, 40, 0, 1], ["Camille", 1, 1, 1, 0, 0, 34, 5, 0],
                            ["Yan", 1, 0, 0, 0, 1, 8, 0, 1]  ],

        [ "bruler", # grands parents abs
                        ["George", 1, 0, 1, 0, 0, 40, 0, 1], ["Emilie", 1, 1, 0, 0, 0, 34, 5, 0],
                            ["Augustin", 1, 0, 1, 0, 0, 10, 0, 0] ]
          ]

    execute = True
    argc = len(argv)
    while argc > argv_count:
        if (parcing()):
            execute = False
            break
        argv_count += 1

    while execute:
        execute = False
        try:
            data = pd.read_csv("/Users/pro/Documents/perso/IA /Netflix/dataset/Dataset.csv", engine='python', sep = ',')
        except:
            print("ERROR : NO_DATA")
            break

        init(Entree, data)
        len_users = len(USERS)
        break_index = int(len_users - len_users * 0.1)
        j = randint(break_index, len_users-1)

        training(USERS[:break_index], [ USERS[j].age, USERS[j].bac, USERS[j].sexe ])
        print("It will be :")
        USERS[j].affich()
    
