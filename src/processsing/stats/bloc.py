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
def analyse_detaillee_par_site(df:pd.DataFrame) -> dict: 

    # Analyse des sites 
    site_counts = df["Site"].value_counts()
    total_site_counts = site_counts.sum()

    # Analyse de la DAP
    dap_colum = "Image and Fluoroscopy Dose Area Product (mGy.cm2)"
    dap_mean_by_site = df.groupby("Site")[dap_colum].mean()
    dap_median_by_site = df.groupby("Site")[dap_colum].median()

    # Analyse du Kair
    kair_column = "Total Air Kerma (mGy)"
    kair_mean_by_site = df.groupby("Site")[kair_column].mean()

    # Analyse du temps de scopie
    time_of_scopy_column = "Total Time of Fluoroscopy (s)"
    time_of_scopy_mean_by_site = df.groupby("Site")[time_of_scopy_column].mean()

    # Analyse des altertes
    alert_column = "Raised alerts?"
    alert_by_site = (df[alert_column]=="Yes").groupby(df["Site"]).sum()


    site_rows = [
        {"site": name, 
        "examen": format_number(int(count)), 
        "pourcentage_exam_by_site": "" if pd.isna((int(count)/total_site_counts)*100) else format_number(round((int(count)/total_site_counts)*100, 1)),
        "mean_DAP": "" if pd.isna(dap_mean_by_site[name]) else format_number(round(dap_mean_by_site[name])),
        "median_DAP": "" if pd.isna(dap_median_by_site[name]) else format_number(round(dap_median_by_site[name])),
        "mean_kair": "" if pd.isna(kair_mean_by_site[name]) else format_number(round(kair_mean_by_site[name])), 
        "mean_time_of_scopy": "" if pd.isna(time_of_scopy_mean_by_site[name]) else format_number(round(time_of_scopy_mean_by_site[name])),
        "number_alert": "" if pd.isna(alert_by_site[name]) else format_number(round(alert_by_site[name])), 
        "pourcentage_alert_by_site": "" if pd.isna((alert_by_site[name]/total_site_counts)*100) else format_number(round((alert_by_site[name]/total_site_counts)*100, 2))
        }
        for name, count in site_counts.items()
    ]

    return site_rows


def analyse_detaillee_par_equipement(df:pd.DataFrame) -> dict: 

    #Analyse des équipements
    device_counts = df["AE Title"].value_counts()
    total_device_counts = device_counts.sum()

    # Analyse de la DAP
    dap_colum = "Image and Fluoroscopy Dose Area Product (mGy.cm2)"
    dap_mean_by_site = df.groupby("AE Title")[dap_colum].mean()

    # Analyse du Kair
    kair_column = "Total Air Kerma (mGy)"
    kair_mean_by_site = df.groupby("AE Title")[kair_column].mean()

    # Analyse du temps de scopie
    time_of_scopy_column = "Total Time of Fluoroscopy (s)"
    time_of_scopy_mean_by_site = df.groupby("AE Title")[time_of_scopy_column].mean()

    # Analyse des altertes
    alert_column = "Raised alerts?"
    alert_by_site = (df[alert_column]=="Yes").groupby(df["AE Title"]).sum()


    device_rows = [
        {"device": name, 
        "model": df.loc[df["AE Title"] == name, "Model"].iloc[0],
        "manufacturer": df.loc[df["AE Title"] == name, "Manufacturer"].iloc[0],
        "nbr_examen": count,
        "mean_DAP": "" if pd.isna(dap_mean_by_site[name]) else format_number(round(dap_mean_by_site[name])),
        "mean_kair": "" if pd.isna(kair_mean_by_site[name]) else format_number(round(kair_mean_by_site[name])), 
        "mean_time_of_scopy": "" if pd.isna(time_of_scopy_mean_by_site[name]) else format_number(round(time_of_scopy_mean_by_site[name])),
        "number_alert": "" if pd.isna(alert_by_site[name]) else format_number(round(alert_by_site[name])), 
        "pourcentage_alert_by_site": "" if pd.isna((alert_by_site[name]/total_device_counts)*100) else format_number(round((alert_by_site[name]/total_device_counts)*100, 2))
        }
        for name, count in device_counts.items()
    ]

    return device_rows



def statistics(df: pd.DataFrame) -> dict: 

    # Card vue d'ensemble 
    nbr_line, min_date, max_date, nbr_years, nbr_device, average_exam_per_year, nbr_site, nbr_dose_alert, percentage_nbr_dose_alert = vue_ensemble_generale(df)

    # Tableau statistique
    average_DAP, median_DAP, Q75_DAP, Q90_DAP, Q95_DAP, max_DAP = indicateurs_dosimetriques_globaux(df, "Image and Fluoroscopy Dose Area Product (mGy.cm2)")
    average_Kair, median_Kair, Q75_Kair, Q90_Kair, Q95_Kair, max_Kair = indicateurs_dosimetriques_globaux(df, "Total Air Kerma (mGy)")
    average_time_of_scopie, median_time_of_scopie, Q75_time_of_scopie, Q90_time_of_scopie, Q95_time_of_scopie, max_time_of_scopie = indicateurs_dosimetriques_globaux(df, "Total Time of Fluoroscopy (s)")
    
    # Tableau d'analyse détaillée par site
    site_rows = analyse_detaillee_par_site(df)

    # Tableau d'analyse détaillée par équipement
    device_rows = analyse_detaillee_par_equipement(df)

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

        "sites": site_rows,
        "devices": device_rows,


    }

    

    return stats_bloc_operatoire
    