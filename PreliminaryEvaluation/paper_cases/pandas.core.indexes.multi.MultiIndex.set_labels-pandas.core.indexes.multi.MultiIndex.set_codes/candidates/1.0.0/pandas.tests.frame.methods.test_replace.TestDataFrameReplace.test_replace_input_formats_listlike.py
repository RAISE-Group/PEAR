def test_replace_input_formats_listlike(self):
    to_rep = {'A': np.nan, 'B': 0, 'C': ''}
    values = {'A': 0, 'B': -1, 'C': 'missing'}
    df = DataFrame({'A': [np.nan, 0, np.inf], 'B': [0, 2, 5], 'C': ['', 'asdf', 'fd']})
    filled = df.replace(to_rep, values)
    expected = {k: v.replace(to_rep[k], values[k]) for k, v in df.items()}
    tm.assert_frame_equal(filled, DataFrame(expected))
    result = df.replace([0, 2, 5], [5, 2, 0])
    expected = DataFrame({'A': [np.nan, 5, np.inf], 'B': [5, 2, 0], 'C': ['', 'asdf', 'fd']})
    tm.assert_frame_equal(result, expected)
    values = {'A': 0, 'B': -1, 'C': 'missing'}
    df = DataFrame({'A': [np.nan, 0, np.nan], 'B': [0, 2, 5], 'C': ['', 'asdf', 'fd']})
    filled = df.replace(np.nan, values)
    expected = {k: v.replace(np.nan, values[k]) for k, v in df.items()}
    tm.assert_frame_equal(filled, DataFrame(expected))
    to_rep = [np.nan, 0, '']
    values = [-2, -1, 'missing']
    result = df.replace(to_rep, values)
    expected = df.copy()
    for i in range(len(to_rep)):
        expected.replace(to_rep[i], values[i], inplace=True)
    tm.assert_frame_equal(result, expected)
    msg = 'Replacement lists must match in length\\. Expecting 3 got 2'
    with pytest.raises(ValueError, match=msg):
        df.replace(to_rep, values[1:])