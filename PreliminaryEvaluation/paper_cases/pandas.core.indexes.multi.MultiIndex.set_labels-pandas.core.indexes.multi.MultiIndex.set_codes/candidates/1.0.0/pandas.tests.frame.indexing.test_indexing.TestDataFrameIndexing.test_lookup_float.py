def test_lookup_float(self, float_frame):
    df = float_frame
    rows = list(df.index) * len(df.columns)
    cols = list(df.columns) * len(df.index)
    result = df.lookup(rows, cols)
    expected = np.array([df.loc[r, c] for r, c in zip(rows, cols)])
    tm.assert_numpy_array_equal(result, expected)