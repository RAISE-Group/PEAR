def test_float_suffix(self):
    df = pd.DataFrame({'treatment_1.1': [1.0, 2.0], 'treatment_2.1': [3.0, 4.0], 'result_1.2': [5.0, 6.0], 'result_1': [0, 9], 'A': ['X1', 'X2']})
    expected = pd.DataFrame({'A': ['X1', 'X1', 'X1', 'X1', 'X2', 'X2', 'X2', 'X2'], 'colname': [1, 1.1, 1.2, 2.1, 1, 1.1, 1.2, 2.1], 'result': [0.0, np.nan, 5.0, np.nan, 9.0, np.nan, 6.0, np.nan], 'treatment': [np.nan, 1.0, np.nan, 3.0, np.nan, 2.0, np.nan, 4.0]})
    expected = expected.set_index(['A', 'colname'])
    result = wide_to_long(df, ['result', 'treatment'], i='A', j='colname', suffix='[0-9.]+', sep='_')
    tm.assert_frame_equal(result, expected)