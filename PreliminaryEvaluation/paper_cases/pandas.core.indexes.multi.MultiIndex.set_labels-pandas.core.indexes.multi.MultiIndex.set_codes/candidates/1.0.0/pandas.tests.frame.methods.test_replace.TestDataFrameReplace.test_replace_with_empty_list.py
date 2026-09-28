def test_replace_with_empty_list(self):
    s = pd.Series([['a', 'b'], [], np.nan, [1]])
    df = pd.DataFrame({'col': s})
    expected = df
    result = df.replace([], np.nan)
    tm.assert_frame_equal(result, expected)
    with pytest.raises(ValueError, match='cannot assign mismatch'):
        df.replace({np.nan: []})
    with pytest.raises(ValueError, match='cannot assign mismatch'):
        df.replace({np.nan: ['dummy', 'alt']})