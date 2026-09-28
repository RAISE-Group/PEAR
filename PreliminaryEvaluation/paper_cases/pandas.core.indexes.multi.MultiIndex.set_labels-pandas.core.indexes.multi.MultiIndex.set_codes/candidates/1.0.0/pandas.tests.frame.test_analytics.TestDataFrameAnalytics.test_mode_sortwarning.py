def test_mode_sortwarning(self):
    df = DataFrame({'A': [np.nan, np.nan, 'a', 'a']})
    expected = DataFrame({'A': ['a', np.nan]})
    with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
        result = df.mode(dropna=False)
        result = result.sort_values(by='A').reset_index(drop=True)
    tm.assert_frame_equal(result, expected)