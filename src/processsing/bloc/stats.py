import pandas as pd 

def bloc_statistics(data_file: str) -> pd.DataFrame: 

    df = pd.read_csv(data_file, low_memory=False)
    
    # Période analysée 
    df["Study date (YYYY-MM-DD)"] = pd.to_datetime(df["Study date (YYYY-MM-DD)"])
    min_date = df["Study date (YYYY-MM-DD)"].min()
    max_date = df["Study date (YYYY-MM-DD)"].max()

    print(list(df["Device"].unique()))

    stats_bloc_operatoire = {
        "nombre de lignes analysées": len(df),
        "période analysée": f"""{min_date.year} - {max_date.year}""",
        "nombre d'équipement": df["AE Title"].nunique(),
    }
    
    return stats_bloc_operatoire
    