import pandas as pd

def limiting(df):
    region_list = ["노원구", "성북구", "강북구"]
    new = df[df["구정보"].isin(region_list)]
    print(new)
