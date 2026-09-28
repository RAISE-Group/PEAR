def test_empty_method(self):
    s_empty = pd.Series(dtype=object)
    assert s_empty.empty
    s2 = pd.Series(index=[1], dtype=object)
    for full_series in [pd.Series([1]), s2]:
        assert not full_series.empty