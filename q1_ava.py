import argparse
if __name__=='__main__':
    parser = argparse.ArgumentParser("Calcul de la puissance d'un nombre.")
    parser.add_argument("-n", "--number", type= int, help= "base (entier)", required= True)
    parser.add_argument("-e", "--exponent", type= int, help="puissance (entier)", default=1)
    args = parser.parse_args()

    result = args.n**args.e
    print(f"Résultat de {args.n} à la puissance {args.e} est: {result}")
