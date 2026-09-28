def test_df_mod_zero_series_does_not_commute(self):
    df = pd.DataFrame(np.random.randn(10, 5))
    ser = df[0]
    res = ser % df
    res2 = df % ser
    assert not res.fillna(0).equals(res2.fillna(0))