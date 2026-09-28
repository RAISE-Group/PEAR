def test_merge_left_notempty_right_empty(self):
    left = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
    right = pd.DataFrame(columns=['x', 'y', 'z'])
    exp_out = pd.DataFrame({'a': [1, 4, 7], 'b': [2, 5, 8], 'c': [3, 6, 9], 'x': np.array([np.nan] * 3, dtype=object), 'y': np.array([np.nan] * 3, dtype=object), 'z': np.array([np.nan] * 3, dtype=object)}, columns=['a', 'b', 'c', 'x', 'y', 'z'])
    exp_in = exp_out[0:0]
    exp_in.index = exp_in.index.astype(object)

    def check1(exp, kwarg):
        result = pd.merge(left, right, how='inner', **kwarg)
        tm.assert_frame_equal(result, exp)
        result = pd.merge(left, right, how='right', **kwarg)
        tm.assert_frame_equal(result, exp)

    def check2(exp, kwarg):
        result = pd.merge(left, right, how='left', **kwarg)
        tm.assert_frame_equal(result, exp)
        result = pd.merge(left, right, how='outer', **kwarg)
        tm.assert_frame_equal(result, exp)
        for kwarg in [dict(left_index=True, right_index=True), dict(left_index=True, right_on='x'), dict(left_on='a', right_index=True), dict(left_on='a', right_on='x')]:
            check1(exp_in, kwarg)
            check2(exp_out, kwarg)