class Noeud:
    def __init__(self, cle):
        self.cle = cle

class Arbre:
    def __init__(self, cle):
        self.Sag = None
        self.Sad = None
        self.racine = Noeud(cle)

    def afficher(self,niveau=0):
        print((' '*niveau)+self.racine.cle)
        if self.Sag:
            self.Sag.afficher(niveau+1)
        if self.Sad:
            self.Sad.afficher(niveau+1)


    def taille(self):
        nb=1
        if self.Sag:
            nb=nb+self.Sag.taille()
        if self.Sad:
            nb=nb+self.Sad.taille()
        return nb
    
    def hauteur(self,niveau=1):
        if self.Sag:
            hg = self.Sag.hauteur(niveau+1)
        else:
            hg = 0
        if self.Sad:
            hd = self.Sad.hauteur(niveau+1)
        else:
            hd = 0
        return max(niveau,hg,hd)
    
    def afficher_prefixe(self):
        res = [self.racine.cle]
        if self.Sag:
            res.extend(self.Sag.afficher_prefixe())
        if self.Sad:
            res.extend(self.Sad.afficher_prefixe())
        return res

    def afficher_infixe(self):
        res = []
        if self.Sag:
            res.extend(self.Sag.afficher_infixe())
        res.extend(self.racine.cle)
        if self.Sad:
            res.extend(self.Sad.afficher_infixe())
        return res

    def afficher_postfixe(self):
        res = []
        if self.Sag:
            res.extend(self.Sag.afficher_postfixe())
        if self.Sad:
            res.extend(self.Sad.afficher_postfixe())
        res.extend(self.racine.cle)
        return res

    def parcours_largeur(self):
        res=[self]
        res_index=0
        while res_index < len(res):
            if res[res_index].Sag:
                res.append(res[res_index].Sag)
            if res[res_index].Sad:
                res.append(res[res_index].Sad)
            res_index += 1
        for i in range(len(res)):
            res[i] = res[i].racine.cle
        return res

    def recherche(self,nombre):
        if self.racine.cle==nombre:
            return True
        else:
            if self.Sag:
                if self.Sag.recherche(nombre):
                    return True
            if self.Sad:
                if self.Sad.recherche(nombre):
                    return True
        return False
    
# Alimentation de l'arbre
a = Arbre('A')
a.Sag = Arbre('B')
a.Sad = Arbre('E')
a.Sag.Sag = Arbre('C')
a.Sag.Sad = Arbre('D')
a.Sad.Sag = Arbre('F')
a.Sad.Sad = Arbre('G')
a.Sad.Sad.Sag = Arbre('H')
a.Sad.Sad.Sad = Arbre('I')
# a.afficher()
print('Taille='+str(a.taille()))
print('Hauteur='+str(a.hauteur()))
print("Afficher en prefixe="+','.join(a.afficher_prefixe()))
print("Afficher en infixe="+','.join(a.afficher_infixe()))
print("Afficher en postfixe="+','.join(a.afficher_postfixe()))
print("Parcours en largeur="+','.join(a.parcours_largeur()))

a = Arbre(15)
a.Sag = Arbre(6)
a.Sad = Arbre(18)
a.Sag.Sag = Arbre(2)
a.Sag.Sad = Arbre(13)
a.Sad.Sag = Arbre(16)
a.Sad.Sad = Arbre(25)
a.Sad.Sad.Sag = Arbre(22)
a.Sad.Sad.Sad = Arbre(26)
print('Recherche de 22='+str(a.recherche(22)))
print('Recherche de 20='+str(a.recherche(20)))

a = Arbre('dfifi')
a.Sag = Arbre('annieji')
a.Sad = Arbre('helene')
a.Sag.Sag = Arbre('aalice')
a.Sag.Sad = Arbre('celine')
print('Recherche de 20='+str(a.recherche(20)))
print('Taille du dico de Entreprise='+str(a.taille()))
print('Hauteur du dico de Entreprise='+str(a.hauteur()))
# Ajout de davidbg et de papicoeur
#
# 
#             davidbg 
#          /            \
#     annieji            helene
#    /       \          /     \
#  aalice   celine   dfifi     papicoeur
#
# Pour faire un affichage dans l'ordre lexicographique, on doit faire un parcours en Infixe (feuille gauche puis racine puis feuille droite)

class ABR:
    
    def present(self, identifiant):
        if self.est_vide():
            return False
        if self.racine() == identifiant:
            return True
        elif self.racine() < identifiant :
            return self.sd().present(identifiant)
        else:
            return self.sg().present(identifiant)
        