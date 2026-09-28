@pytest.mark.parametrize('index', tm.all_index_generator(10))
def test_map_empty(self, index):
    s = Series(index)
    result = s.map({})
    expected = pd.Series(np.nan, index=s.index)
    tm.assert_series_equal(result, expected)