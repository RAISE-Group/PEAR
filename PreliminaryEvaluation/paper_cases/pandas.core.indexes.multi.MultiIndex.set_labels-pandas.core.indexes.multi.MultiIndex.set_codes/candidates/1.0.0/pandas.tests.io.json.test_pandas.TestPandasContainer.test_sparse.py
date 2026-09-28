def test_sparse(self):
    df = pd.DataFrame(np.random.randn(10, 4))
    df.loc[:8] = np.nan
    sdf = df.astype('Sparse')
    expected = df.to_json()
    assert expected == sdf.to_json()
    s = pd.Series(np.random.randn(10))
    s.loc[:8] = np.nan
    ss = s.astype('Sparse')
    expected = s.to_json()
    assert expected == ss.to_json()