import config 
from src.preprocessing.file_reader import read_file
from src.preprocessing.tests_management import manage_tests
from src.report.report_generation import html_content

RADIOLOGIE_INTERVENTIONNELLE_CARDIOLOGIE = config.RADIOLOGIE_INTERVENTIONNELLE_CARDIOLOGIE
RADIOLOGIE_INTERVENTIONNELLE_NEURORADIOLOGIE_VASCULAIRE = config.RADIOLOGIE_INTERVENTIONNELLE_NEURORADIOLOGIE_VASCULAIRE
SCANNERS = config.SCANNERS
RADIOLOGIE_CONVENTIONNELLE = config.RADIOLOGIE_CONVENTIONNELLE
MAMMOGRAPHIE = config.MAMMOGRAPHIE
RADIOLOGIE_DENTAIRE = config.RADIOLOGIE_DENTAIRE
BLOC_OPERATOIRE = config.BLOC_OPERATOIRE
MEDECINE_NUCEAIRE = config.MEDECINE_NUCEAIRE


# Ajouter dentaire, medecine nucléaire et neuroradiologie vasculaire


CSV_RADIOLOGIE_INTERVENTIONNELLE_CARDIOLOGIE = config.CSV_RADIOLOGIE_INTERVENTIONNELLE_CARDIOLOGIE
CSV_RADIOLOGIE_INTERVENTIONNELLE_NEUROLOGIE_VASCULAIRE = config.CSV_RADIOLOGIE_INTERVENTIONNELLE_NEURORADIOLOGIE_VASCULAIRE
CSV_SCANNERS = config.CSV_SCANNERS
CSV_RADIOLOGIE_CONVENTIONNELLE = config.CSV_RADIOLOGIE_CONVENTIONNELLE
CSV_MAMMOGRAPHIE = config.CSV_MAMMOGRAPHIE
CSV_RADIOLOGIE_DENTAIRE = config.CSV_RADIOLOGIE_DENTAIRE
CSV_BLOC_OPERATOIRE = config.CSV_BLOC_OPERATOIRE
CSV_MEDECINE_NUCEAIRE = config.CSV_MEDECINE_NUCEAIRE


def main(): 

    # Lecutre des fichiers Excel puis enregistrement au format csv dans le dossier data (à run une fois au début)
    
    #read_file(RADIOLOGIE_INTERVENTIONNELLE_CARDIOLOGIE, "Interventional data export", CSV_RADIOLOGIE_INTERVENTIONNELLE_CARDIOLOGIE)
    #read_file(SCANNERS, "scanners", CSV_SCANNERS)
    #read_file(RADIOLOGIE_CONVENTIONNELLE, "conventionnel", CSV_RADIOLOGIE_CONVENTIONNELLE)
    #read_file(MAMMOGRAPHIE, "senologie", CSV_MAMMOGRAPHIE)
    #read_file(BLOC_OPERATOIRE, "GLOBAL", CSV_BLOC_OPERATOIRE)

    # Suppression des lignes test 
    #df_radiologie_interventionnelle_cardiologie = manage_tests(CSV_RADIOLOGIE_INTERVENTIONNELLE_CARDIOLOGIE)
    #df_scanners = manage_tests(CSV_SCANNERS)
    #df_radiologie_conventionnelle = manage_tests(CSV_RADIOLOGIE_CONVENTIONNELLE)
    #df_mammographie = manage_tests(CSV_MAMMOGRAPHIE)
    #df_bloc_operatoire = manage_tests(CSV_BLOC_OPERATOIRE)

    with open("dashboard.html", "w", encoding="utf-8") as f: 
        f.write(html_content)


if __name__ == "__main__": 
    main()