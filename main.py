import config 
from src.preprocessing.file_reader import read_file

BLOC_OPERATOIRE = config.BLOC_OPERATOIRE

def main(): 

    df = read_file(BLOC_OPERATOIRE, "GLOBAL")


if __name__ == "__main__": 
    main()