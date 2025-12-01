import pandas as pd 


def manage_tests(data_file: str) -> pd.DataFrame:

    df = pd.read_csv(data_file, low_memory=False)

    df = df[df["Patient sex"] != "OTHER"]
    df = df[~df["Patient ID"].astype(str).str.contains(r"[a-zA-Z-]", na=False)]

    return df 