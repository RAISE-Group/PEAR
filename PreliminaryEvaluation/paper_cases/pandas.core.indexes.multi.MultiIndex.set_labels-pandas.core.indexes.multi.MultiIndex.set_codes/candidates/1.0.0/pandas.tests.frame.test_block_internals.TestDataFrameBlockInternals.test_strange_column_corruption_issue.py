def test_strange_column_corruption_issue(self):
    df = DataFrame(index=[0, 1])
    df[0] = np.nan
    wasCol = {}
    for i, dt in enumerate(df.index):
        for col in range(100, 200):
            if col not in wasCol:
                wasCol[col] = 1
                df[col] = np.nan
            df[col][dt] = i
    myid = 100
    first = len(df.loc[pd.isna(df[myid]), [myid]])
    second = len(df.loc[pd.isna(df[myid]), [myid]])
    assert first == second == 0