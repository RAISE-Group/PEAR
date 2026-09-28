def test_map_callable(self):
    index = self.create_index()
    expected = index + index.freq
    result = index.map(lambda x: x + x.freq)
    tm.assert_index_equal(result, expected)
    result = index.map(lambda x: pd.NaT if x == index[0] else x)
    expected = pd.Index([pd.NaT] + index[1:].tolist())
    tm.assert_index_equal(result, expected)