import pandas as pd

def read_csv(file="bonn.csv", perc_name="bonn_perc"):

    d = pd.read_csv(file, delimiter=";", usecols=[0, 1], names=[perc_name, "timestamp"], skiprows=1)
    d["timestamp"] = pd.to_datetime(d["timestamp"], unit="s")
    d.set_index("timestamp", inplace=True)
    print(d)
    return d





if __name__ == '__main__':
    df_b = read_csv()
    df_beul = read_csv("./beuel.csv", "beuel_perc")

    df_b_h = df_b.resample("30min").mean()
    df_beul_h = df_beul.resample("30min").mean()

    df_total = pd.merge(df_b_h, df_beul_h, left_index=True, right_index=True, how="inner")

    print(df_total)

    grouped_df = df_total.groupby(df_b_h.index.time)

    print(grouped_df)
    for g_name, g_data in grouped_df:
        print(g_data["bonn_perc"])

