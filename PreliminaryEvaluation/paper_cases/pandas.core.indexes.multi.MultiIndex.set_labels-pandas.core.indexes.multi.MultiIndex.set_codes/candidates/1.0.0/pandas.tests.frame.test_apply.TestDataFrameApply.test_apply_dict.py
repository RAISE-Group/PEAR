def test_apply_dict(self):
    A = DataFrame([['foo', 'bar'], ['spam', 'eggs']])
    A_dicts = Series([dict([(0, 'foo'), (1, 'spam')]), dict([(0, 'bar'), (1, 'eggs')])])
    B = DataFrame([[0, 1], [2, 3]])
    B_dicts = Series([dict([(0, 0), (1, 2)]), dict([(0, 1), (1, 3)])])
    fn = lambda x: x.to_dict()
    for df, dicts in [(A, A_dicts), (B, B_dicts)]:
        reduce_true = df.apply(fn, result_type='reduce')
        reduce_false = df.apply(fn, result_type='expand')
        reduce_none = df.apply(fn)
        tm.assert_series_equal(reduce_true, dicts)
        tm.assert_frame_equal(reduce_false, df)
        tm.assert_series_equal(reduce_none, dicts)