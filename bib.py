import json
class Livre:
    #dunder
    def __init__(self):
        self.titre = 'title'
        self.auteur = 'author'
        self.contenu = 'content'
        self.id = 'id'
        
    @property
    def title(self):
        return self.title
    @title.setter
    def title(self, value):
        if len(value) < 5:
            print('Le titre doit contenir au moins 5 caractères')
            self.title = value


class Utilisateur:
    def __init__(self):
        self.nom = 'nom'
        self.id = 'id'
        self.idLivre = 'idLivre'


class Librairie:
    def __init__(self):
        self.id = 'id'
        self.idLivre = 'idLivre'
        self.idBib = 'idBib'

class Bibliotheque:
    def __init__(self):
        self.id = 'id'
        self.idLivre = 'idLivre'
        self.idLibrairie = 'idLibrairie'
        self.idUtilisateur = 'idUtilisateur'

if __name__ == '__main__': 

    d = Livre()
    print("Titre : ", d.titre)
    d.titre = 't'
    print("Titre : ",d.titre)
