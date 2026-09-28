def test_nested_dict_overlapping_keys_replace_str(self):
    a = np.arange(1, 5)
    astr = a.astype(str)
    bstr = np.arange(2, 6).astype(str)
    df = DataFrame({'a': astr})
    result = df.replace(dict(zip(astr, bstr)))
    expected = df.replace({'a': dict(zip(astr, bstr))})
    tm.assert_frame_equal(result, expected)