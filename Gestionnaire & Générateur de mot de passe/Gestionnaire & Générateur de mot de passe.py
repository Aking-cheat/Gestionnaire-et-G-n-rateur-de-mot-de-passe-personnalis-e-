
import random
from termcolor import *
import string


def main():

    answer = input(colored("1. Générer un mot de passe\n2. Gestionnaire de mot de passe\n\nEntrer un chiffre: ", 'blue'))
    if answer == "1":
        gen_mdp()
    if answer == "2":
        gest_mdp()

def gen_mdp():
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#$%^&*()")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    def generate_random_password():
        length = int(input("Entrer la longeur souhaiter de votre mot de passe: "))

        alphabets_count = int(input("Entrer le nombre de lettres souhaiter: "))
        digits_count = int(input("Entrer le nombre de chiffres souhaiter: "))
        special_characters_count = int(input("Entrer le nombre de caractère spéciaux: "))

        characters_count = alphabets_count + digits_count + special_characters_count

        if characters_count > length:
            print("La somme de vos choix ne font pas la longeur souhaiter")
            return

        password = []

        for i in range(alphabets_count):
            password.append(random.choice(alphabets))

        for i in range(digits_count):
            password.append(random.choice(digits))

        for i in range(special_characters_count):
            password.append(random.choice(special_characters))

        if characters_count < length:
            random.shuffle(characters)
            for i in range(length - characters_count):
                password.append(random.choice(characters))

        random.shuffle(password)

        print(colored("".join(password).center(50), 'cyan'))
        print(colored("✔✔✔ 👆👆 Votre mot de passe a été générer 👆👆 ✔✔✔", 'green'))

    generate_random_password()
def gest_mdp():
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    *** = "PASSWORD"
    answer = input(colored("1. ***\n2. ***\n3. ***\n4. ***\n5. ***\n6. ***\n7. ***\n8. ***\n9. ***\n10. ***\n11. ***\n12. ***\nEntrez un chiffre: ", 'yellow'))
    if answer == "1":
        print(colored(***, 'red'))
    if answer == "2":
        print(colored(***, 'red'))
    if answer == "3":
        print(colored(***, 'red'))
    if answer == "4":
        print(colored(***, 'red'))
    if answer == "5":
        print(colored(***, 'red'))
    if answer == "6":
        print(colored(***, 'red'))
    if answer == "7":
        print(colored(***, 'red'))
    if answer == "8":
        print(colored(***, 'red'))
    if answer == "9":
        print(colored(***, 'red'))
    if answer == "10":
        print(colored(***, 'red'))
    if answer == "11":
        print(colored(***, 'red'))
    if answer == "12":
        print(colored("exemple1: " + *** + "\nexemple2: " + *** + "\nexemple3: " + *** + "\nexemple3: " + *** + "\nexemple4: " + *** + "\nexemple5: " + *** + "\nexemple6: " + *** + "\nexemple7: " + *** + "\nexemple8: " + *** + "\nexemple9: " + *** + "\nexemple10: " + ***, 'red'))
if __name__ == '__main__':
    main()