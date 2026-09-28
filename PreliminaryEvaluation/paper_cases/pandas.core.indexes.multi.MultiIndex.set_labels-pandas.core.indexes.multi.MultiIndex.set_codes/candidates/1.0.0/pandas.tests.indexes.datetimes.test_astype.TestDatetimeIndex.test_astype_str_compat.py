def test_astype_str_compat(self):
    idx = DatetimeIndex(['2016-05-16', 'NaT', NaT, np.NaN])
    result = idx.astype(str)
    expected = Index(['2016-05-16', 'NaT', 'NaT', 'NaT'], dtype=object)
    tm.assert_index_equal(result, expected)