import random
import time

# définition de la classe générique Pokemon
class Pokemon:
    # définition du constructeur grâce à la méthode __init__
    def __init__(self, nom, type_, points_de_vie):
        self.nom = nom
        self.type_ = type_
        self.points_de_vie = points_de_vie

    # définition de la fonction pour afficher les infos du pokemon
    def afficher_info(self):
        print(f"Nom: {self.nom}, Type: {self.type_}, Points de vie: {self.points_de_vie}")

    # définition de la fonction pour vérifier si le pokemon est vaincu
    def est_vaincu(self):
        return self.points_de_vie <= 0

    # définition de la fonction pour attaquer un autre pokemon
    def attaquer(self, autre_pokemon, degats=5):
        autre_pokemon.points_de_vie -= degats
        if autre_pokemon.points_de_vie < 0:
            autre_pokemon.points_de_vie = 0
        print(f"  {self.nom} attaque {autre_pokemon.nom} et inflige {degats} degats! {autre_pokemon.nom} a {autre_pokemon.points_de_vie} PV restants.")

# définition des classes pour les différents types de pokemons
# Il est demandé de définir une classe pour chaque type de pokémon, qui hérite de la classe Pokemon
# Chaque classe doit redéfinir la méthode attaquer pour ajouter des attaques spécifiques à chaque type de pokémon
# Uniquement pour l'exercice car on pourrait mutualiser du code en remontant la fonctionnalité sur la classe mère 
class PokemonElectrique(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 3 # degats infligés par défaut
        if random.randint(1, 3) == 3: # 1 chance sur 3 de réussir l'attaque éclair
            degats = 10 # degats infligés en plus si attaque eclair réussie
        if random.randint(1, 2) == 1: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"   -> {self.nom} rate son attaque.")

class PokemonFeu(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 5 # degats infligés par défaut
        if random.randint(1, 6) == 6: # 1 chance sur 6 de réussir l'attaque flamme
            degats = 15
        if random.randint(1, 2) == 1: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"   -> {self.nom} rate son attaque.")

class PokemonEau(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 7 # degats infligés par défaut
        if random.randint(1, 5) == 5: # 1 chance sur 6 de réussir l'attaque noyade
            degats = 10
        if random.randint(1, 2) == 2: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"   -> {self.nom} rate son attaque.")

class PokemonPlante(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 15 # degats infligés par défaut
        if random.randint(1, 15) == 15: # 1 chance sur 15 de réussir l'attaque fouet
            degats = 20
        if random.randint(1, 2) == 2: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"   -> {self.nom} rate son attaque.")

class PokemonFee(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 8 # degats infligés par défaut
        if random.randint(1, 4) == 4: # 1 chance sur 4 de réussir l'attaque charme
            degats = 12
        if random.randint(1, 2) == 2: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"{self.nom} rate son attaque.")

class PokemonSpectre(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 8 # degats infligés par défaut
        if random.randint(1, 6) == 6: # 1 chance sur 6 de réussir l'attaque hypnose
            degats = 12
        if random.randint(1, 2) == 2: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"{self.nom} rate son attaque.")

class PokemonPsy(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 8 # degats infligés par défaut
        if random.randint(1, 6) == 6: # 1 chance sur 6 de réussir l'attaque hypnose
            degats = 11 # degats infligés par défaut
        if random.randint(1, 2) == 2: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"{self.nom} rate son attaque.")

class PokemonNormal(Pokemon):
    def attaquer(self, autre_pokemon):
        degats = 8 # degats infligés par défaut
        if random.randint(1, 6) == 6:
            degats = 9 # degats infligés par défaut
        if random.randint(1, 2) == 2: # 1 chance sur 2 de réussir son attaque
            super().attaquer(autre_pokemon, degats)  # Appelle la fonction attaquer de la classe parent
        else:
            print(f"{self.nom} rate son attaque.")

# Fonction pour simuler un duel entre deux Pokémon
def duel(pokemon1, pokemon2): # pokemon1 et pokemon2 sont les deux Pokémon qui s'affrontent
    print("")
    print(f"*********** Duel entre {pokemon1.nom} et {pokemon2.nom}! ***********")
    tour = 0
    while not pokemon1.est_vaincu() and not pokemon2.est_vaincu(): #creation d'une boucle pour que le combat continue jusqu'à ce qu'un des pokemons soit vaincu
        print("")
        print(f"        ******* Round {tour} *******")
        if tour % 2 == 0: # si le reste de la division de tour par 2 est égal à 0, pokemon1 attaque, sinon pokemon2 attaque
            pokemon1.attaquer(pokemon2) # pokemon1 attaque pokemon2 avec 20 points de dégats
        else:
            pokemon2.attaquer(pokemon1) # pokemon2 attaque pokemon1 avec 20 points de dégats
        print(f"    A l'issu du combat {pokemon1.nom} a {pokemon1.points_de_vie} PV, {pokemon2.nom} a {pokemon2.points_de_vie} PV")
        tour += 1 # augmente de 1 le tour, pour pas que se soit toujours le même pokemon qui attaque
        

###############################################
############# Programme principal #############
###############################################
# Création des instances de Pokémon
pikachu = PokemonElectrique("Pikachu", "Electrique", 35) # creation de pikachu qui est un pokemon de type electrique avec 35 points de vie
salameche = PokemonFeu("Salameche", "Feu", 30) # creation de salameche qui est un pokemon de type feu avec 30 points de vie
carapuce = PokemonEau("Carapuce", "Eau", 32) # creation de carapuce qui est un pokemon de type eau avec 32 points de vie
bulbizarre = PokemonPlante("Bulbizarre", "Plante", 33) # creation de bulbizarre qui est un pokemon de type plante avec 33 points de vie
rondoudou = PokemonFee("Rondoudou", "Fee", 25) # creation de rondoudou qui est un pokemon de type fée avec 25 points de vie
phantominus = PokemonSpectre("Phantominus", "Spectre", 30) # creation de phantominus qui est un pokemon de type spectre avec 30 points de vie
ronflex = Pokemon("Ronflex", "Normal", 40) # creation de ronflex qui est un pokemon de type normal avec 40 points de vie
Lokhlass = Pokemon("Lokhlass", "Eau", 35) # creation de Lokhlass qui est un pokemon de type eau avec 35 points de vie
Mewtwo = Pokemon("Mewtwo", "Psy", 40) # creation de Mewtwo qui est un pokemon de type psy avec 40 points de vie
Ténéfix = Pokemon("Tenefix", "Spectre", 35) # creation de Ténéfix qui est un pokemon de type spectre avec 35 points de vie

# Affichage des informations des Pokémon
pikachu.afficher_info() # affiche les informations du pokemon pikachu (nom, type, points de vie)
salameche.afficher_info() # affiche les informations du pokemon salameche (nom, type, points de vie)
carapuce.afficher_info() # affiche les informations du pokemon carapuce (nom, type, points de vie)
bulbizarre.afficher_info() # affiche les informations du pokemon bulbizarre (nom, type, points de vie)
rondoudou.afficher_info() # affiche les informations du pokemon rondoudou (nom, type, points de vie)
phantominus.afficher_info() # affiche les informations du pokemon phantominus (nom, type, points de vie)
ronflex.afficher_info() # affiche les informations du pokemon ronflex (nom, type, points de vie)
Lokhlass.afficher_info() # affiche les informations du pokemon Lokhlass (nom, type, points de vie)
Mewtwo.afficher_info() # affiche les informations du pokemon Mewtwo (nom, type, points de vie)
Ténéfix.afficher_info() # affiche les informations du pokemon Ténéfix (nom, type, points de vie)

print ("") 
print ("") 
print ("****************************************************************") # affiche le titre du tournoi
print ("********************* Tournoi de pokemons **********************") # affiche le titre du tournoi
print ("****************************************************************") # affiche le titre du tournoi
print ("") 
# Liste des Pokémon
pokemons = [pikachu, salameche, carapuce, bulbizarre, rondoudou, phantominus, ronflex, Lokhlass, Mewtwo, Ténéfix] # liste des pokemons qui participent au tournoi

# Boucle du tournoi
while len(pokemons) > 1: # tant qu'il reste plus d'un pokemon dans la liste, le tournoi continue

    # Tirage au sort des deux pokemons qui vont s'affronter
    pokemon1_index = random.randint(0, len(pokemons) - 1)
    pokemon2_index = random.randint(0, len(pokemons) - 1)
    while pokemon1_index == pokemon2_index :    # On vérifie que les deux pokemons ne sont pas les mêmes
        pokemon2_index = random.randint(0, len(pokemons) - 1)
    pokemon1 = pokemons[pokemon1_index] # pokemon1 est un pokemon aléatoire de la liste des pokemons
    pokemon2 = pokemons[pokemon2_index] # pokemon2 est un pokemon aléatoire de la liste des pokemons

    duel(pokemon1, pokemon2) # appelle la fonction duel pour faire s'affronter les pokemons 2 par 2 dans la liste des pokemons
    if pokemon1.est_vaincu(): # si le pokemon1 est vaincu, pokemon2 est ajouté à la liste des gagnants, sinon pokemon1 est ajouté à la liste des gagnants
        print("")
        print(f"   ==> {pokemon2.nom} remporte le duel contre {pokemon1.nom} ! ")
        print("")
        pokemons.pop(pokemon1_index) # supprime le pokemon1 de la liste des pokemons
        pokemon2.points_de_vie = min(pokemon2.points_de_vie + 10, 35)  # Récupération de points de vie du gagnant
    else:
        print("")
        print(f"   ==> {pokemon1.nom} remporte le duel contre {pokemon2.nom} ! ")
        print("")
        pokemons.pop(pokemon2_index) # supprime le pokemon2 de la liste des pokemons
        pokemon1.points_de_vie = min(pokemon1.points_de_vie + 10, 35)  # Récupération de points de vie du gagnant

# Déclaration du vainqueur
print ("")
print ("") 
print ("") 
print ("****************************************************************") 
print(f"       Le champion du tournoi est {pokemons[0].nom}! ")
print ("****************************************************************") 
