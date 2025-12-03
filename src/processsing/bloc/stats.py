import pandas as pd 

def bloc_statistics(df: pd.DataFrame) -> dict: 

    # Nombre de lignes analysées 
    nbr_line = len(df)

    # Période analysée 
    df["Study date (YYYY-MM-DD)"] = pd.to_datetime(df["Study date (YYYY-MM-DD)"])
    min_date = df["Study date (YYYY-MM-DD)"].dt.year.min()
    max_date = df["Study date (YYYY-MM-DD)"].dt.year.max()

    # Nombre d'équipement 
    nbr_device = df["AE Title"].nunique()

    # Moyenne d'examen par an 
    average_exam_per_year = round(df.groupby(df["Study date (YYYY-MM-DD)"].dt.year).size().mean())

    stats_bloc_operatoire = {
        "nombre de lignes analysées": nbr_line,
        "période analysée": f"""{min_date} - {max_date}""",
        "nombre d'équipement": nbr_device,
        "moyenne d'examen par an": average_exam_per_year
    }
    
    return stats_bloc_operatoire
    