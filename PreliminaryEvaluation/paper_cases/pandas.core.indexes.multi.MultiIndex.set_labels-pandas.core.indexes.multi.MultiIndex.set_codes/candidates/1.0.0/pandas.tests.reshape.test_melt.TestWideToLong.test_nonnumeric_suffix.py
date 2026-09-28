def test_nonnumeric_suffix(self):
    df = pd.DataFrame({'treatment_placebo': [1.0, 2.0], 'treatment_test': [3.0, 4.0], 'result_placebo': [5.0, 6.0], 'A': ['X1', 'X2']})
    expected = pd.DataFrame({'A': ['X1', 'X1', 'X2', 'X2'], 'colname': ['placebo', 'test', 'placebo', 'test'], 'result': [5.0, np.nan, 6.0, np.nan], 'treatment': [1.0, 3.0, 2.0, 4.0]})
    expected = expected.set_index(['A', 'colname'])
    result = wide_to_long(df, ['result', 'treatment'], i='A', j='colname', suffix='[a-z]+', sep='_')
    tm.assert_frame_equal(result, expected)