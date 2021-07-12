from sys import argv
from random import randint
from profile import profile
import Process, Thread

# Create the people's profiles.
# The structure is : name, action, horreur, policier, romantique, dessin_anime, age, bac, sexe
def init(famille):
    for j in famille:
        for i in j[1:]:
            try:
                USERS.append( profile( i[0] + " " + j[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]) )
            except:
                print(j[0] + ' ' + i[0])

# Create the help menu
doc_name = "cli.py"
def help():
    print("-------------------------------------------- help --------------------------------------------")
    print("")
    print("python " + doc_name + " : show the prediction of a profile and the reality")
    print("")
    print("Options :")
    print("-c, -confidence : show the confidence")
    print("-h, -help : show this message and stop the programm")
    print("-n, -name name : change the name of the csv file name")
    print("-p, -process int : change the default number of heart use (6 by default)")
    print("-t, -thread int : use the threading module and no more the processing module. Nbr optionnal")
    print("-T, -train int : make the training 'int' times")

    # Execute the training of the IA
def training(lst_users, to_predict):
    global ia, population, name, train, show_confidence
    
    # Whith using the multiprocessing module ...
    if ia == "process":
        Einstein = Process.Foret(population, name, show_confidence)
    # ... or the multithreading mudule
    else:
        Einstein = Thread.Foret(population, name, show_confidence)

    Einstein.training(lst_users, train)
    print("The prediction is :")
    Einstein.prediction(to_predict)

# Parce the Command Line
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
                population = int(argv[argv_count])
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
        elif argv[argv_count][1:] == "confidence" or argv[argv_count][1:] == "c":
            global show_confidence
            show_confidence = True
    

# Inicialising globals
USERS = []
ia = "process"
population = 6
argv_count = 1
name = "poid"
train = 0
show_confidence = False


if __name__ == "__main__":
    # Create some Family
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
    
    # Annalyse the Command Line and quit if the help module is show.
    quit = True
    argc = len(argv)
    while argc > argv_count:
        if (parcing()):
            quit = False
            break
        argv_count += 1

    if quit:
        init(Entree) # Create the DB
        
        # We're using 80% of the DB to the training and 20% to take an unknown profil
        len_users = len(USERS)
        boucle = int(len_users - len_users * 0.2)
        j = randint(boucle, len_users-1)

        # Make x times the training. The varrable is "train" and is by default 0
        training(USERS[:boucle], [ USERS[j].age, USERS[j].bac, USERS[j].sexe ])
        print("It will be :")
        USERS[j].affich()
    
