def test_replace_input_formats_scalar(self):
    df = DataFrame({'A': [np.nan, 0, np.inf], 'B': [0, 2, 5], 'C': ['', 'asdf', 'fd']})
    to_rep = {'A': np.nan, 'B': 0, 'C': ''}
    filled = df.replace(to_rep, 0)
    expected = {k: v.replace(to_rep[k], 0) for k, v in df.items()}
    tm.assert_frame_equal(filled, DataFrame(expected))
    msg = 'value argument must be scalar, dict, or Series'
    with pytest.raises(TypeError, match=msg):
        df.replace(to_rep, [np.nan, 0, ''])
    to_rep = [np.nan, 0, '']
    result = df.replace(to_rep, -1)
    expected = df.copy()
    for i in range(len(to_rep)):
        expected.replace(to_rep[i], -1, inplace=True)
    tm.assert_frame_equal(result, expected)