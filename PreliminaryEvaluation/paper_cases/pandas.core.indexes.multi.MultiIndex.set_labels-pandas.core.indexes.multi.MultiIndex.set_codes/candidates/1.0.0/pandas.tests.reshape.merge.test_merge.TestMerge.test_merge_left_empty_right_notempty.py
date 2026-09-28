def test_merge_left_empty_right_notempty(self):
    left = pd.DataFrame(columns=['a', 'b', 'c'])
    right = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['x', 'y', 'z'])
    exp_out = pd.DataFrame({'a': np.array([np.nan] * 3, dtype=object), 'b': np.array([np.nan] * 3, dtype=object), 'c': np.array([np.nan] * 3, dtype=object), 'x': [1, 4, 7], 'y': [2, 5, 8], 'z': [3, 6, 9]}, columns=['a', 'b', 'c', 'x', 'y', 'z'])
    exp_in = exp_out[0:0]
    exp_in.index = exp_in.index.astype(object)

    def check1(exp, kwarg):
        result = pd.merge(left, right, how='inner', **kwarg)
        tm.assert_frame_equal(result, exp)
        result = pd.merge(left, right, how='left', **kwarg)
        tm.assert_frame_equal(result, exp)

    def check2(exp, kwarg):
        result = pd.merge(left, right, how='right', **kwarg)
        tm.assert_frame_equal(result, exp)
        result = pd.merge(left, right, how='outer', **kwarg)
        tm.assert_frame_equal(result, exp)
    for kwarg in [dict(left_index=True, right_index=True), dict(left_index=True, right_on='x')]:
        check1(exp_in, kwarg)
        check2(exp_out, kwarg)
    kwarg = dict(left_on='a', right_index=True)
    check1(exp_in, kwarg)
    exp_out['a'] = [0, 1, 2]
    check2(exp_out, kwarg)
    kwarg = dict(left_on='a', right_on='x')
    check1(exp_in, kwarg)
    exp_out['a'] = np.array([np.nan] * 3, dtype=object)
    check2(exp_out, kwarg)