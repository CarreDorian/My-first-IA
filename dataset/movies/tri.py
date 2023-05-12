import pandas as pd

movies_cols = ['MovieID','Title','Genres']
ratings_cols = ['UserID','MovieID','Rating','Timestamp']
users_cols = ['UserID','Gender','Age','Occupation','Zip-code']

movies = pd.read_csv("/Users/pro/Documents/perso/IA /Netflix/dataset/movies/movies.dat", engine='python', sep = '::',header = None, names = movies_cols, encoding = 'latin 1')
ratings = pd.read_csv("/Users/pro/Documents/perso/IA /Netflix/dataset/movies/ratings.dat", engine='python', sep = '::', header = None, names = ratings_cols, encoding = 'latin 1')
users = pd.read_csv("/Users/pro/Documents/perso/IA /Netflix/dataset/movies/users.dat", engine='python', sep = '::', header = None, names = users_cols, encoding = 'latin 1')

columns=['UserID','action','horreur','policier','romantique','dessin_anime','age','bac','sexe']
BDD = pd.DataFrame(columns=columns)

movies['Genres'] = movies['Genres'].str.split('|')
filmGenre = {'action' : ["Adventure", 'Action', 'Western', 'War'],
             'horreur' : ["Thriller", 'Horror'],
             'policier' : ["Crime", 'Mystery'],
             'romantique' : ["Romance", 'Drama'],
             'dessin_anime' : ["Children's", 'Animation']}

for i in movies.index:
    for replace_genre in filmGenre.keys():
        is_genre = False
        for sub_genre in filmGenre[replace_genre]:
            if (sub_genre in movies['Genres'][i]):
                movies['Genres'][i].remove(sub_genre)
                is_genre = True
        if (is_genre):
            movies['Genres'][i].append(replace_genre)

    for replace_genre in ['Comedy', 'Fantasy', 'Sci-Fi', 'Documentary', 'Musical', 'Film-Noir']:
        if (replace_genre in movies['Genres'][i]):
            movies['Genres'][i].remove(replace_genre)

    if (len(movies['Genres'][i]) == 0):
        movies = movies.drop(i)


for userID in ratings['UserID'].unique():
    data = ratings[ratings.UserID == userID]
    gouts = {'action' : 0,
             'horreur' : 0,
             'policier' : 0,
             'romantique' : 0,
             'dessin_anime' : 0}
    nbr_films = 0

    for index in data.index:
        filmID = data['MovieID'][index]
        film = movies[movies.MovieID == filmID]
        if len(film.Genres.values) == 0:
            continue
        for genre in film.Genres.values[0]:
            if int(data['Rating'][index]) > 3:
                gouts[str(genre)] += 1
        
        nbr_films += 1
    
    hight_values = 0
    for val in gouts.values():
        if hight_values < val:
            hight_values = int(val)
    
    hight_values /= 4

    user = users[users.UserID == userID]
    sexe = 0
    if (user.Gender.values[0] == "M"):
        sexe = 1
    dic = {'UserID':userID, 'age':user.Age.values[0], 'bac':user.Occupation.values[0], 'sexe':sexe}  
    for key in gouts.keys():
        key = str(key)
        if gouts[key] >= hight_values:
            gouts[key] = 1
        else:
            gouts[key] = 0
            
        dic[key] = gouts[key]

    BDD = BDD.append(dic, ignore_index=True)

BDD.to_csv('../Dataset.csv', index=False)
