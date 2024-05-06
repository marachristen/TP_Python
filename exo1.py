from functools import reduce

#question 1, Définir sous la forme d’une fonction lambda [] Doc.], une fonction triple renvoyant le triple d’un nombre.
triple = lambda x: x*3
print (triple(3))

#question 2
est_pair = lambda x: x%2==0
print(est_pair(4))
print(est_pair(7))

#question 3
def multiplicateur(n):
    return lambda x: x*n
print(multiplicateur(4)(2))

#question 4
print([x for x in range(10)if x%2!=0])
print(list(filter(lambda x: x%2!=0, range(10))))

#question5
print([x*3 for x in range(1,11)])
print(list(map(lambda x: x*3, range(1,11))))

#question6
print([x*3 for x in range(11) if x%2==0])
print(list(map(lambda x: x*3,filter(lambda x: x%2==0, range(11)))))

#question7
produit = lambda x,y: x*y
print(reduce(produit, range(1,11)))

#question8
factorial = lambda n: reduce(lambda x,y: x*y, range(1,n+1),1)
print(factorial(10))

#question9
l = ['a','b','c']
print('_'.join(l))
print(reduce(lambda x,y:x+'_'+y,l))

#question10
def pair(l):
    return{x:x%2==0 for x in l}
print(pair([1,4,3,7,8]))

#question11
l = ["un","deux","trois"]
print(f"{l[1]}:\n{l[0]};{l[2]}!") #n heisst nach une, und t isch en tab nach rechts

#question12
def extraire_longs_mots(sentence):
    #split retourne d liste vode wörter wo vome espace trennt sind
    #lower macht eif alles lowercase
    words = [word.lower() for word in sentence.split(' ') if len(word)>3]
    words = sorted(words) #sorted duts par défaut alphabetisch ordne
    return ';'.join(words)
print(extraire_longs_mots('Je Suis Contente'))



