def test_stubs(self):
    df = pd.DataFrame([[0, 1, 2, 3, 8], [4, 5, 6, 7, 9]])
    df.columns = ['id', 'inc1', 'inc2', 'edu1', 'edu2']
    stubs = ['inc', 'edu']
    df_long = pd.wide_to_long(df, stubs, i='id', j='age')
    assert stubs == ['inc', 'edu']