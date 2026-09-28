def test_pass_datetimeindex_to_index(self):
    rng = date_range('1/1/2000', '3/1/2000')
    idx = Index(rng, dtype=object)
    expected = Index(rng.to_pydatetime(), dtype=object)
    tm.assert_numpy_array_equal(idx.values, expected.values)