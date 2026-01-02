from data import limiting
import pandas as pd

def main():
    df = pd.read_csv("25_first_half.csv")
    new = limiting(df)
    print(new)

if __name__ == "__main__":
    main()