import pandas as pd 


# Permet de mettre un espace tous les trois chiffres pour plus de lisibilité
def format_number(n):
    return f"{n:,}".replace(",", " ")


# Card de vue d'ensemble générale
def vue_ensemble_generale(df:pd.DataFrame) -> float: 

    # Nombre de lignes analysées 
    nbr_line = format_number(len(df))

    # Période analysée 
    df["Study date (YYYY-MM-DD)"] = pd.to_datetime(df["Study date (YYYY-MM-DD)"])
    min_date = df["Study date (YYYY-MM-DD)"].dt.year.min()
    max_date = df["Study date (YYYY-MM-DD)"].dt.year.max()

    nbr_years = format_number(max_date-min_date)

    # Nombre d'équipement 
    nbr_device = format_number(df["AE Title"].nunique())

    # Moyenne d'examen par an 
    average_exam_per_year = format_number(round(df.groupby(df["Study date (YYYY-MM-DD)"].dt.year).size().mean()))

    # Nombre de sites analysés
    nbr_site = format_number(df["Site"].nunique())

    # Nombre d'alerte de doses 
    nbr_dose_alert = float(format_number((df["Raised alerts?"]=="Yes").sum()))
    percentage_nbr_dose_alert = format_number(round(nbr_dose_alert/len(df["Raised alerts?"])*100, 2))

    return nbr_line, min_date, max_date, nbr_years, nbr_device, average_exam_per_year, nbr_site, nbr_dose_alert, percentage_nbr_dose_alert



# Tableau d'indicateurs dosimétriques globaux
def indicateurs_dosimetriques_globaux(df:pd.DataFrame, column_name: str) -> float:
    # Moyenne
    average= format_number(round((df[column_name]).mean(), 2))
    # Médiane 
    median = format_number(round((df[column_name]).median(), 2))
    # Q75
    Q75 = format_number(round((df[column_name]).quantile(0.75), 2))
    # Q90 
    Q90 = format_number(round((df[column_name]).quantile(0.90), 2))
    # Q95
    Q95 = format_number(round((df[column_name]).quantile(0.95), 2))
    # Max
    max = format_number(round((df[column_name]).max(), 2))

    return average, median, Q75, Q90, Q95, max



# Tableau d'analyse détaillée par site
def analyse_detaillee_par_site(df:pd.DataFrame) -> float: 

    site = df["Site"].value_counts().to_dict()
    return site 

def bloc_statistics(df: pd.DataFrame) -> dict: 

    # Card vue d'ensemble 
    nbr_line, min_date, max_date, nbr_years, nbr_device, average_exam_per_year, nbr_site, nbr_dose_alert, percentage_nbr_dose_alert = vue_ensemble_generale(df)

    # Tableau statistique
    average_DAP, median_DAP, Q75_DAP, Q90_DAP, Q95_DAP, max_DAP = indicateurs_dosimetriques_globaux(df, "Image and Fluoroscopy Dose Area Product (mGy.cm2)")
    average_Kair, median_Kair, Q75_Kair, Q90_Kair, Q95_Kair, max_Kair = indicateurs_dosimetriques_globaux(df, "Total Air Kerma (mGy)")
    average_time_of_scopie, median_time_of_scopie, Q75_time_of_scopie, Q90_time_of_scopie, Q95_time_of_scopie, max_time_of_scopie = indicateurs_dosimetriques_globaux(df, "Total Time of Fluoroscopy (s)")

    # Tbaleau analyse détaillée par site
    site = analyse_detaillee_par_site(df)


    stats_bloc_operatoire = {
        "nombre_de_lignes_analysées": nbr_line,
        "période_analysée": f"""{min_date} - {max_date}""",
        "nombre_années_analysées": nbr_years,
        "nombre_équipement": nbr_device,
        "moyenne_examen_par_an": average_exam_per_year, 
        "nombre_de_site": nbr_site,
        "nombre_alerte_de_doses": nbr_dose_alert, 
        "pourcentage_alerte_de_doses": percentage_nbr_dose_alert,

        "moyenne_DAP": average_DAP,
        "mediane_DAP": median_DAP,
        "Q75_DAP": Q75_DAP, 
        "Q90_DAP": Q90_DAP,
        "Q95_DAP": Q95_DAP,
        "max_DAP": max_DAP, 

        "moyenne_Kair": average_Kair,
        "mediane_Kair": median_Kair,
        "Q75_Kair": Q75_Kair, 
        "Q90_Kair": Q90_Kair,
        "Q95_Kair": Q95_Kair,
        "max_Kair": max_Kair, 

        "moyenne_temps_de_scopie": average_time_of_scopie,
        "mediane_temps_de_scopie": median_time_of_scopie,
        "Q75_temps_de_scopie": Q75_time_of_scopie, 
        "Q90_temps_de_scopie": Q90_time_of_scopie,
        "Q95_temps_de_scopie": Q95_time_of_scopie,
        "max_temps_de_scopie": max_time_of_scopie, 

    }
    
    return stats_bloc_operatoire
    