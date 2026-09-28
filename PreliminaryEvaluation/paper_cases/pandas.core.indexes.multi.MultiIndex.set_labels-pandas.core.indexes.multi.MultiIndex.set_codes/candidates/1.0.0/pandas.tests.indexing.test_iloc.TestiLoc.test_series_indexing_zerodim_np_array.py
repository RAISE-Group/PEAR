def test_series_indexing_zerodim_np_array(self):
    s = Series([1, 2])
    result = s.iloc[np.array(0)]
    assert result == 1