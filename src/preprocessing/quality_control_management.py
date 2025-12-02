import pandas as pd 


def manage_quality_control(data_file: str) -> pd.DataFrame:

    df = pd.read_csv(data_file, low_memory=False)

    # Suppression des lignes qui ont un sex=OTHER et un NIP avec des lettres ou des tirets
    df = df[df["Patient sex"] != "OTHER"]
    df = df[~df["Patient ID"].astype(str).str.contains(r"[a-zA-Z-]", na=False)]

    # Suppression des NIP pour l'anonymisation 
    df = df.drop(columns=["Patient ID", "Study Instance UID", "Study ID", "Accession number"])

    return df 