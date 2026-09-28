def test_df_float_none_comparison(self):
    df = pd.DataFrame(np.random.randn(8, 3), index=range(8), columns=['A', 'B', 'C'])
    result = df.__eq__(None)
    assert not result.any().any()