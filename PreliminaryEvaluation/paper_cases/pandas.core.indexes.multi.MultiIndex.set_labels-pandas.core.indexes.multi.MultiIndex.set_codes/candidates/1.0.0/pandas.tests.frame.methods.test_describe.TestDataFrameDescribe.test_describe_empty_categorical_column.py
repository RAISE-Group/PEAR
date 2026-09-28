def test_describe_empty_categorical_column(self):
    df = pd.DataFrame({'empty_col': Categorical([])})
    result = df.describe()
    expected = DataFrame({'empty_col': [0, 0, np.nan, np.nan]}, index=['count', 'unique', 'top', 'freq'], dtype='object')
    tm.assert_frame_equal(result, expected)
    assert np.isnan(result.iloc[2, 0])
    assert np.isnan(result.iloc[3, 0])