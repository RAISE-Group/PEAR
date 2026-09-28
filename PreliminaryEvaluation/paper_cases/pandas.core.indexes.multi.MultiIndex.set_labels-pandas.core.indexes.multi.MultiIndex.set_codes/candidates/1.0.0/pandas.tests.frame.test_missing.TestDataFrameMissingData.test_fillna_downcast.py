def test_fillna_downcast(self):
    df = pd.DataFrame({'a': [1.0, np.nan]})
    result = df.fillna(0, downcast='infer')
    expected = pd.DataFrame({'a': [1, 0]})
    tm.assert_frame_equal(result, expected)
    df = pd.DataFrame({'a': [1.0, np.nan]})
    result = df.fillna({'a': 0}, downcast='infer')
    expected = pd.DataFrame({'a': [1, 0]})
    tm.assert_frame_equal(result, expected)