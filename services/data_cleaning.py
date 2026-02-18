def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df
