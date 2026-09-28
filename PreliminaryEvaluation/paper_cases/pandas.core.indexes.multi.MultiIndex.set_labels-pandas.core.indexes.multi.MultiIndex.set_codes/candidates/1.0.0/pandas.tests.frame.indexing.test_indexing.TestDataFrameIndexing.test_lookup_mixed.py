def test_lookup_mixed(self, float_string_frame):
    df = float_string_frame
    rows = list(df.index) * len(df.columns)
    cols = list(df.columns) * len(df.index)
    result = df.lookup(rows, cols)
    expected = np.array([df.loc[r, c] for r, c in zip(rows, cols)], dtype=np.object_)
    tm.assert_almost_equal(result, expected)