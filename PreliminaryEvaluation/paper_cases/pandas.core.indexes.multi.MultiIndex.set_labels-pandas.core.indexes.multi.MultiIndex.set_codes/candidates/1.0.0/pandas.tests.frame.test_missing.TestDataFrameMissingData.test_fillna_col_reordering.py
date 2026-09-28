def test_fillna_col_reordering(self):
    cols = ['COL.' + str(i) for i in range(5, 0, -1)]
    data = np.random.rand(20, 5)
    df = DataFrame(index=range(20), columns=cols, data=data)
    filled = df.fillna(method='ffill')
    assert df.columns.tolist() == filled.columns.tolist()