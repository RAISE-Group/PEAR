def test_values_mixed_dtypes(self, float_frame, float_string_frame):
    frame = float_frame
    arr = frame.values
    frame_cols = frame.columns
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            col = frame_cols[j]
            if np.isnan(value):
                assert np.isnan(frame[col][i])
            else:
                assert value == frame[col][i]
    arr = float_string_frame[['foo', 'A']].values
    assert arr[0, 0] == 'bar'
    df = DataFrame({'complex': [1j, 2j, 3j], 'real': [1, 2, 3]})
    arr = df.values
    assert arr[0, 0] == 1j
    arr = float_frame[['A', 'B']].values
    expected = float_frame.reindex(columns=['A', 'B']).values
    tm.assert_almost_equal(arr, expected)