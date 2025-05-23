from math import *
from matplotlib.pyplot import *
import random

def lire_temperature_max_fichier(nom_fichier):
    """
    Cette fonction lit un fichier contenant des données de températures par jour pour les années entre 2012 et 2022 de la ville de Montréal.
    Elle récupère les températures maximales pour chaque jour de chaque mois de chaque année.
    :param nom_fichier: Le nom du fichier contenant les données de températures pour les années entre 2012 et 2022.
    :return: Un dictionnaire contenant les températures maximales : Année -> Mois -> Temp Max (Pour tous les jours)
    """
    temp_max = {}

    with open(nom_fichier, "r") as fichier:

        for ligne in fichier:

            if ligne[0] == "!":
                continue

            annee, mois, jour, tmax, _ = ligne.strip().split(",")  # Ignorer la température minimale

            if tmax != ' Missing' and 2012 <= int(annee) <= 2022:
                if annee not in temp_max:
                    temp_max[annee] = {}  # Dictionnaire pour chaque année

                if mois not in temp_max[annee]:
                    temp_max[annee][mois] = []  # Liste pour chaque mois de l'année

                temp_max[annee][mois].append(float(tmax))

    return temp_max
def lire_temperature_min_fichier(nom_fichier):
    """
    Cette fonction lit un fichier contenant des données de températures par jour pour les années entre 2012 et 2022 de la ville de Montréal.
    Elle récupère les températures minimales pour chaque jour de chaque mois de chaque année.
    :param nom_fichier: Le nom du fichier contenant les données de températures pour les années entre 2012 et 2022.
    :return: Un dictionnaire contenant les températures minimales : Année -> Mois -> Temp Min (Pour tous les jours)
    """
    temp_min = {}

    with open(nom_fichier, "r") as fichier:

        for ligne in fichier:

            if ligne[0] == "!":
                continue

            annee, mois, jour, _, tmin = ligne.strip().split(",")  # Ignorer la température maximale

            if tmin != ' Missing' and 2012 <= int(annee) <= 2022:
                if annee not in temp_min:
                    temp_min[annee] = {}  # Dictionnaire pour chaque année

                if mois not in temp_min[annee]:
                    temp_min[annee][mois] = []  # Liste pour chaque mois de l'année

                temp_min[annee][mois].append(float(tmin))

    return temp_min
def calculer_moyenne_par_mois(temperature):
    """
    Cette fonction calcule les moyennes mensuelles des températures maximales ou minimales à partir des données fournies.
    Les valeurs manquantes ont déjà été trié précédemment (voir fonctions de lecture de températures)
    :param temperature: Un dictionnaire contenant les données de températures maximales ou minimales.
    La structure attendue est Année -> Mois -> Temp Max ou Année -> Mois -> Temp Min.
    :return: Un dictionnaire avec les moyennes mensuelles des températures pour chaque mois de chaque année : Mois -> [Moyenne Température].
    Les moyennes seront stockées dans l'ordre chronologique des années (2012, 2013, ...)
    """
    moyenne_mois = {}

    # Initialise le dictionnaire moyenne_mois avec des listes vides pour chaque mois
    for mois in range(1, 13):
        moyenne_mois[mois] = []

    # Calcule les moyennes mensuelles à partir des données de température
    for annee in temperature:
        for mois in temperature[annee]:
            temperatures_mensuelles = temperature[annee][mois]
            temperature_moyenne = round(sum(temperatures_mensuelles) / len(temperatures_mensuelles), 1)
            moyenne_mois[int(mois)].append(temperature_moyenne)

    return moyenne_mois
def tracer_graphique_temperature_moyenne_maximale_en_fonction_du_mois_selon_annee():
    # Calculer les moyennes par mois pour les températures maximales
    moyennes_max = calculer_moyenne_par_mois(lire_temperature_max_fichier("donnees_complete.txt"))

    # Créer un graphique
    figure(figsize=(10, 6))

    # Couleurs et styles pour distinction
    custom_colors = ['brown', 'teal', 'tomato', 'aquamarine', 'orange', 'purple', 'cyan', 'mediumorchid', 'dodgerblue', 'pink', 'red']
    custom_line_styles = ['-', '--', '-.', ':']

    # Plot pour chaque année
    for annee in range(2012, 2023):
        temperatures_annee = [moyennes_max[mois][annee - 2012] for mois in moyennes_max.keys()]
        plot(range(1, 13), temperatures_annee,
             marker = 'o',
             linestyle = custom_line_styles[random.randint(0, len(custom_line_styles) - 1)],
             label = f'Année {annee}',
             color = custom_colors[2022 - annee])

    # Settings du graphique
    title('Température Maximale Moyenne par Mois de 2012 à 2022')
    xlabel('Mois')
    ylabel('Température (°C)')
    xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Dec'])
    legend()
    grid(True)
    show()
def tracer_graphique_temperature_moyenne_minimale_en_fonction_du_mois_selon_annee():
    # Calculer les moyennes par mois pour les températures minimales
    moyennes_min = calculer_moyenne_par_mois(lire_temperature_min_fichier("donnees_complete.txt"))

    # Créer un graphique
    figure(figsize=(10, 6))

    # Couleurs et styles pour distinction
    custom_colors = ['brown', 'teal', 'tomato', 'aquamarine', 'orange', 'purple', 'cyan', 'mediumorchid', 'dodgerblue', 'pink', 'red']
    custom_line_styles = ['-', '--', '-.', ':']

    # Plot pour chaque année
    for annee in range(2012, 2023):
        temperatures_annee = [moyennes_min[mois][annee - 2012] for mois in moyennes_min.keys()]
        plot(range(1, 13), temperatures_annee,
             marker = 'o',
             linestyle = custom_line_styles[random.randint(0, len(custom_line_styles) - 1)],
             label = f'Année {annee}',
             color = custom_colors[2022 - annee])

    # Settings du graphique
    title('Température Minimale Moyenne par Mois de 2012 à 2022')
    xlabel('Mois')
    ylabel('Température (°C)')
    xticks(range(1, 13), ['Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Dec'])
    legend()
    grid(True)
    show()

def meteo_montreal(fichier):
    """
    La fonction permet de lire un fichier .csv ou .txt
     et trouver la moyenne des températures minimales/maximales
     pour chaque mois de chaque année puis les représenter
     dans un graphique selon le choix de l'utilisateur (min ou max)
    :param fichier: un fichier .csv ou .txt qui contient les données.
    :return: None
    """
    # Demander à l'utilisateur quelle température il souhaite visualiser
    choix = input("Voulez-vous voir les graphiques pour les températures maximales (max) ou minimales (min) ? Entrez 'max' ou 'min': ")

    # Afficher le graphique contenant les courbes max/min selon le choix
    if choix == 'max':
        tracer_graphique_temperature_moyenne_maximale_en_fonction_du_mois_selon_annee()
    elif choix == 'min':
        tracer_graphique_temperature_moyenne_minimale_en_fonction_du_mois_selon_annee()
    else:
        print("Choix invalide. Veuillez entrer 'max' ou 'min'.")

meteo_montreal("donnees_complete.txt")



