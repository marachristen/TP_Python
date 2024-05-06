#question1
def lister_int(n):
    return ','.join([str(x) for x in range(1,n+1)])
print(lister_int(10))
# out: 1,2,3,4,5,6,7,8,9,10

#question2
l1 = ['Albert Troussard', 'Elias Amine', 'Imane Jennane', 'Mathieu Faure', 'Valentin Parisot']
l2 = ['EPFL', 'UNIL', 'EPFL', 'EPFL', 'EPFL']
print('\n'.join([student for (student, school) in list(zip(l1,l2)) if school == 'UNIL']))
# out: Elias Amine

#question3
list_nb = [[2,3,4],[1],[2,7]]
new_list = '/'.join([''.join([str(x) for x in l]) for l in list_nb])
print(new_list)
# out: 234/1/27

#question4
noms=[['John','Ronald','Reuel','Tolkien'],['Noé','Zufferey'],['Claire','Océane','Roxane','Bilat'],
      ['Melike', 'Gwendoline', 'Alice', 'Gecer']]
x = ', '.join([l[0] + (' 'if len(l)>2 else ' ')+''.join(map(lambda s: s[0].capitalize()+'. ',
                                                             l[1:-1]))+''+l[-1]for l in sorted(noms,key=lambda n:n[-1])])
print(x)
# 1. On trie la liste noms par nom de famille (le dernier élément de la liste des noms de chaque individu):
# sorted(noms, key=lambda n: n[−1])
# Sorted permet de trier une liste, le paramètre key prend en entrée une fonction qui sera utilisée
# comme clé permettant de faire le tri. Dans notre cas, la fonction lambda utilisée retourne le dernier
# élément d'une liste (le nom de famille donc)
# 2. Pour chaque individu, on transforme la liste de ses prénoms et noms en une seule chaîne de caractères
# où les prénoms du milieu (l[1:−1]) sont remplacés par leur intiale (la première lettre s[0]): l[0] +
# (' ' if len(l) > 2 else '') + ' '.join(map(lambda s: s[0].capitalize() + '.', l[1:−1])) + ' ' + l[−1]
# 3. On concatène les chaînes de caractères ainsi obtenues en les séparant par des virgules: ', '.join(...)
# out: Claire O. R. Bilat, Melike G. A. Gecer, John R. R. Tolkien, Noé Zufferey

# question5
infractions = [ #prénom, nom et un degré de gravité de l’infraction commise
    ("Edward", "Elric", 5),
    ("Izumi", "Curtis", 9),
    ("King", "Bradley", 0),
    ("Maes", "Hughes", 4)
]
sorted_infractions = sorted(infractions, key=lambda x: x[2], reverse=True)
print(sorted_infractions)
# out: [('Izumi', 'Curtis', 9), ('Edward', 'Elric', 5), ('Maes', 'Hughes', 4), ('King', 'Bradley', 0)]

# question6
dict = {'fruit':'banane','legume':'carotte'}
new_dict = {v: k for k, v in dict.items()}
print(new_dict)
# out: {'banane': 'fruit', 'carotte': 'legume'}

# question7
d1 = {3: 'voiture', 2: 'velo'}
d2 = {3: 'rouge', 1: 'bleu'}
print([{v:d2[k] for k, v in d1.items() if k in d2}])
# out: [{'voiture': 'rouge'}]

# question8
def create_email(s):
    ls = s.strip().split(" ")
    return f"{ls[1]}.{ls[0]}@unil.ch"
l = open("namen.txt").readlines()
print(": ".join(list(map(create_email, l))))
# out: Kevin.Huguenin@unil.ch: Alpha.Diallo@unil.ch: Noe.Zufferey@unil.ch: Lev.Velykoicanenko@unil.ch



