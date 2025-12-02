import pandas as pd 

def clean_columns(data_file: str) -> pd.DataFrame:

    df = pd.read_csv(data_file, low_memory=False)
    df["Device"] = df["Device"].replace("HH2 secteurs ortho / rachis / dig", "HH2 secteur ortho / rachis / dig")

    return df 