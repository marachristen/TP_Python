import argparse, math, sys
if __name__=='__main__':
    parser = argparse.ArgumentParser("Calcul de la racine carrée d'un nombre")
    parser.add_argument("-n", "--number", type=int, help="number (entier)", required=True)
    parser.add_argument("-o", "--output", help="sauvegarde dans resultat.rtf", action="store_true")

    args = parser.parse_args()

    if args.number <0:
        print("la fonction racine n'est pas définie pour les nombres négatifs")
    elif args.output:
        f = open("resultat.rtf", mode="w")
        f.write(f"racine carrée de {args.number} est égal à {math.sqrt(args.number)}\n")
        f.close()
    else:
        print(math.sqrt(args.number)) #f.write iwie ine





