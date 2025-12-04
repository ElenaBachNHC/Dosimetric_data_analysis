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
    nbr_dose_alert = format_number((df["Raised alerts?"]=="Yes").sum())
    percentage_nbr_dose_alert = format_number(round(((df["Raised alerts?"]=="Yes").sum())/len(df["Raised alerts?"])*100, 2))

    return nbr_line, min_date, max_date, nbr_years, nbr_device, average_exam_per_year, nbr_site, nbr_dose_alert, percentage_nbr_dose_alert



def statistics(df: pd.DataFrame) -> dict: 

    # Card vue d'ensemble 
    nbr_line, min_date, max_date, nbr_years, nbr_device, average_exam_per_year, nbr_site, nbr_dose_alert, percentage_nbr_dose_alert = vue_ensemble_generale(df)



    stats_bloc_operatoire = {
        "nombre_de_lignes_analysées": nbr_line,
        "période_analysée": f"""{min_date} - {max_date}""",
        "nombre_années_analysées": nbr_years,
        "nombre_équipement": nbr_device,
        "moyenne_examen_par_an": average_exam_per_year, 
        "nombre_de_site": nbr_site,
        "nombre_alerte_de_doses": nbr_dose_alert, 
        "pourcentage_alerte_de_doses": percentage_nbr_dose_alert,

    }
    
    return stats_bloc_operatoire
    