''' Create Total for each group in pivot table'''
df = pd.concat([
    y.append(y.sum().rename(str(x) + ': Total' ))
    for x, y in df.groupby(level=1)
]).append(df.sum()).transpose()

for c in df.columns:
    if isinstance(c, tuple):
        level, account, desc = c
        df.rename(columns = {c: str(account)+': '+str(desc)}, inplace=True)
        

