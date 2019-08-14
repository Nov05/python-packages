def nov05_colnulls(df):
    colnulls = []
    for col in df:
        count = df[col].isnull().sum()
        colnulls.append(count)
        print("Column", col, "has", count, "null values.")
        
    print('Data frame has', sum(colnulls), 'null values.')
    return colnulls