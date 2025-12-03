import pandas as pd 

def bloc_statistics(df: pd.DataFrame) -> dict: 

    # Nombre de lignes analysées 
    nbr_line = len(df)

    # Période analysée 
    df["Study date (YYYY-MM-DD)"] = pd.to_datetime(df["Study date (YYYY-MM-DD)"])
    min_date = df["Study date (YYYY-MM-DD)"].dt.year.min()
    max_date = df["Study date (YYYY-MM-DD)"].dt.year.max()

    nbr_years = max_date-min_date

    # Nombre d'équipement 
    nbr_device = df["AE Title"].nunique()

    # Moyenne d'examen par an 
    average_exam_per_year = round(df.groupby(df["Study date (YYYY-MM-DD)"].dt.year).size().mean())

    # Nombre de sites analysés
    nbr_site = df["Site"].nunique()

    # Nombre d'alerte de doses 
    nbr_dose_alert = (df["Raised alerts?"]=="Yes").sum()
    percentage_nbr_dose_alert = round(nbr_dose_alert/len(df["Raised alerts?"])*100, 2)

    stats_bloc_operatoire = {
        "nombre de lignes analysées": nbr_line,
        "période analysée": f"""{min_date} - {max_date}""",
        "nombre d'années analysées": nbr_years,
        "nombre d'équipement": nbr_device,
        "moyenne d'examen par an": average_exam_per_year, 
        "nombre de site": nbr_site,
        "nombre d'alerte de doses": nbr_dose_alert, 
        "pourcentage alerte de doses": percentage_nbr_dose_alert,
    }

    
    return stats_bloc_operatoire
    