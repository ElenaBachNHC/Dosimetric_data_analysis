import pandas as pd
from pathlib import Path



def read_file(file_path: str, sheet_name: str): 

    # Conversion du str en path 
    file_path = Path(file_path)

    # Erreur si le fichier n'existe pas
    if not file_path.exists(): 
        raise FileNotFoundError(f"Fichier non trouvé: {file_path}")

    # Lecture du fichier 
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print(f"Le fichier contient {len(df)} lignes et {len(df.columns)} colonnes")

    return df
    
