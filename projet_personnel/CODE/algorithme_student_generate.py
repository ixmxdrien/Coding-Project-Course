#  DATA BASE GENERATING

import pandas as pd
import random
import numpy as np
from faker import Faker

school_years = ['BAC1', 'BAC2', 'BAC3', 'MA1', 'MA2']


place_of_birth = ['Mons', 'Charleroi', 'Tournai', 'La Louvière', 'Namur', 'Nivelles', 'Wavre', "Braine-l'Alleud", 'Waterloo', 'Louvain-la-Neuve',
    'Soignies', 'Thuin', 'Binche', 'Ath', 'Enghien', 'Jodoigne', 'Gembloux', 'Fleurus', 'Sambreville', 'Châtelet',
    'Marche-en-Famenne', 'Dinant', 'Ciney', 'Philippeville', 'Huy', 'Andenne', 'Ottignies-Louvain-la-Neuve', 'Hannut', 'Waremme', 'Fosses-la-Ville',
    'Tubize', 'Nivelles', 'Genappe', 'Jodoigne', 'Ottignies', 'La Hulpe', 'Court-Saint-Étienne', 'Rebecq', 'Wavre', 'Waterloo',
    'Lasne', 'Rixensart', 'Rosières', 'Ittre', 'Braine-le-Château', 'Chaumont-Gistoux', 'Walhain', 'Mont-Saint-Guibert', 'Beauvechain', 'Hélécine']

streets = ['Rue de la Liberté', 'Avenue des Roses', 'Chaussée de Bruxelles', 'Rue du Commerce', 'Avenue du Parc', 'Rue Saint-Pierre', 'Chemin des Cerisiers', 'Boulevard des Étoiles', 'Avenue de la Gare', 'Rue des Champs',
    'Chaussée de Namur', 'Rue de la Paix', 'Avenue des Lilas', 'Rue de la Fontaine', 'Chemin du Moulin', 'Boulevard des Arts', 'Avenue des Mésanges', 'Rue des Orangers', 'Chaussée de Liège', 'Rue de l\'Église',
    'Avenue du Lac', 'Rue des Violettes', 'Chemin des Peupliers', 'Boulevard de la Mer', 'Rue des Platanes', 'Avenue des Acacias', 'Chaussée de Mons', 'Rue de la Rivière', 'Avenue du Soleil', 'Rue des Écoles',
    'Chemin des Pommiers', 'Boulevard des Montagnes', 'Rue des Trois Fontaines', 'Avenue des Cèdres', 'Chaussée de Charleroi', 'Rue du Théâtre', 'Boulevard des Papillons', 'Rue des Primevères', 'Avenue des Charmes', 'Chemin des Saules',
    'Rue du Palais', 'Avenue de la Plage', 'Chaussée de Waterloo', 'Rue des Amandiers', 'Boulevard du Jardin', 'Avenue des Coquelicots', 'Rue des Moulins', 'Chemin des Roses', 'Boulevard de la Forêt', 'Rue des Iris']


gender = ['M', 'F', 'O']


campus_localisation = ["Louvain-la-Neuve", "Mons"]

all_course_BAC1 = ("Anglais 1", "Fondements du droit public", "Fondements du droit de l'entreprise", "Economie", "Espagnol 1", "Comptabilité", "Informatique de gestion", "Mathématiques de gestion 1", "Statistiques et probabilités", "Pilosophie", "Psychologie", "Sociologie", "Séminaire de travail universitaire en gestion")

all_course_BAC2 = ("Anglais 2", "Droit de l'entreprise", "Macroéconomie", "Microéconomie", "Espagnol 2", "Marketing", "Production", "Informatique et algorithmique", "Finance", "Inférences statistiques", "Mathématiques de gestion 2", "Technologies industrielles")

all_course_BAC3 = ("Anglais 3", "Economie industrielle", "Espagnol 3", "Séminaire : organisations et transformation digitale", "Management humain", "Projet entrepreneurial", "Comptabilité et contrôle de gestion", "Gestion de données", "Coding project", "Econométrie", "Recherche opérationnelle", "Optimization", "Séminaire : organisation et mutations sociales", "Questions de sciences religieuses")

all_course_MA1 = ("Advanced English 1", "Español avanzado 1", "Data analytics", "Projet quantitatif et gestion de projet", "Data Mining", "Nouvelles technologies et pratiques émergentes", "Web mining", "Machine learning", "Quantitative Decision Making", "Recommender Systems", "Pilotage stratégique de l'entreprise", "Séminaire on Current Managerial Issues")

all_course_MA2 = ("Advanced English 2", "Español avanzado 1", "Responsabilité sociétale de l'entreprise","Integrated Information Systems", "Mémoire", "Séminaire d'accompagnement du mémoire")


# Définir les proportions souhaitées pour chaque année académique
proportions = [0.4, 0.25, 0.15, 0.1, 0.1]

# Liste des années académiques disponibles
school_years = ['BAC1', 'BAC2', 'BAC3', 'MA1', 'MA2']
# Générer des combinaisons aléatoires de noms et prénoms pour plus de 1000 personnes
data_generated = []

fake = Faker()

number_of_students = 1000

for each in range(number_of_students): # générer des données

    # nom de la personnes
    last_name = fake.last_name()

    # prenom de la personnes
    first_name = fake.first_name()

    # année de cours
    academic_year = np.random.choice(school_years, p=proportions)

    # curriculum
    if academic_year in ['BAC1', 'BAC2', 'BAC3'] :
        curriculum = "INGM1BA"
    else :
        curriculum = "INGM2M"

    # ville de naissance de la personne
    city_of_birth = random.choice(place_of_birth)

    # attribuer un numero de téléphone à la personne
    phone_number = []
    n = f"{random.randint(100000000, 999999999):08d}"
    if n not in phone_number :
      phone_number.append(n)
      phone =  f"0{n[:3]}/{n[3:5]}.{n[5:7]}.{n[7:]}"

    # endroit où habite la personne
    student_city = random.choice(place_of_birth)
    student_street = random.choice(streets)
    student_number_of_house = random.randint(1, 200)
    adress_of_student = f"{student_street} {student_number_of_house}, {student_city}"

    #attribution du sexe d'une personne
    gender_of_student = random.choice(gender)


    #email de la personne
    email_of_student = f"{first_name}{'.'}{last_name}{'@student.uclouvain.be'}"
    email_formated = email_of_student.lower()

    #attribution des campus aux élèves
    campus = random.choice(campus_localisation)

    # date de naissance  sachant que l'on est en 2023 donc qqn de 17 ans ne peut pas se trouver en master
    if academic_year == 'BAC1':
        year_of_birth = 2005
    elif academic_year == 'BAC2':
        year_of_birth = 2004
    elif academic_year == 'BAC3':
        year_of_birth = 2003
    elif academic_year == 'MA1':
        year_of_birth = 2002
    else:
        year_of_birth = 2001

    month_of_birth = random.randint(1, 12)
    day_of_birth = random.randint(1, 28)
    complete_date_of_birth = f"{day_of_birth}/{month_of_birth}/{year_of_birth}"


    # attribution du matricule
    consonant_of_firstname = ''.join([c for c in first_name if c.lower() not in 'aeiou'])[:3]
    consonant_of_lastname = ''.join([c for c in last_name if c.lower() not in 'aeiou'])[:2]
    last_consonant_of_lastname = ''.join([c for c in last_name if c.lower() not in 'aeiou']).lower()[-1] # ne sait pas si c'est la consonne du prénom ou du nom
    year_of_birth_string = str(year_of_birth)[-4:]
    random_integer = random.randint(0, 10)
    matricule = f"{consonant_of_lastname }{consonant_of_firstname}{last_consonant_of_lastname}{year_of_birth_string}{random_integer}"
    matricule = matricule.lower()


    #attribution des notes aléatoirement
    grades = {}
    if academic_year == 'MA2':
        for courses in all_course_BAC1 + all_course_BAC2 + all_course_BAC3 + all_course_MA1:
            grades[courses] = random.randint(10, 20)  # l'éléve a dû réussir ces cours pour pouvoir avoir acces en MA2
        for courses in all_course_MA2 :
            grades[courses] = random.randint(0, 20) # l'éléve pourrait avoir eu entre 0 et 20
    elif academic_year == 'MA1':
        for courses in all_course_BAC1 + all_course_BAC2 + all_course_BAC3 :
            grades[courses] = random.randint(10, 20)
        for courses in all_course_MA1 :
            grades[courses] = random.randint(0, 20)
    elif academic_year == 'BAC3':
        for courses in all_course_BAC1 + all_course_BAC2 :
            grades[courses] = random.randint(10, 20)
        for courses in all_course_BAC3 :
            grades[courses] = random.randint(0, 20)
    elif academic_year == 'BAC2':
        for courses in all_course_BAC1 :
            grades[courses] = random.randint(10, 20)
        for courses in all_course_BAC2 :
            grades[courses] = random.randint(0, 20)
    else:
        for courses in all_course_BAC1:
            grades[courses] = random.randint(0, 20)


    data_generated.append({"Firstname": first_name, "Lastname": last_name, "Academic Year" : academic_year, "Curriculum" : curriculum, "Place of Birth" : city_of_birth , "Telephone": phone, "Address": adress_of_student, "Gender" : gender_of_student, "Email" : email_formated, "Campus" : campus, "Date of Birth" : complete_date_of_birth, "Matricule" : matricule, **grades})

# Créer un DataFrame pandas
df = pd.DataFrame(data_generated)

# Enregistrer le DataFrame dans un fichier Excel
df.to_excel("Data_Base.xlsx", index=False)