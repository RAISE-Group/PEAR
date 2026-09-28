def test_stack_mixed_dtype(self):
    df = self.frame.T
    df['foo', 'four'] = 'foo'
    df = df.sort_index(level=1, axis=1)
    stacked = df.stack()
    result = df['foo'].stack().sort_index()
    tm.assert_series_equal(stacked['foo'], result, check_names=False)
    assert result.name is None
    assert stacked['bar'].dtype == np.float_