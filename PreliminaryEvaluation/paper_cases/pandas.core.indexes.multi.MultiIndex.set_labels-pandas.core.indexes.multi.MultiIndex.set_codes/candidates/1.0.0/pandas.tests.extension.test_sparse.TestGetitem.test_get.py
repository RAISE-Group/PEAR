def test_get(self, data):
    s = pd.Series(data, index=[2 * i for i in range(len(data))])
    if np.isnan(s.values.fill_value):
        assert np.isnan(s.get(4)) and np.isnan(s.iloc[2])
    else:
        assert s.get(4) == s.iloc[2]
    assert s.get(2) == s.iloc[1]