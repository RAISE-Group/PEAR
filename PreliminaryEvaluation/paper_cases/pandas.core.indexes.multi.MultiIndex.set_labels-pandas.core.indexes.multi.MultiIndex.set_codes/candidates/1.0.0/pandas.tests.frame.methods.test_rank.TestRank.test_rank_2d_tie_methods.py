@pytest.mark.parametrize('axis', [0, 1])
@pytest.mark.parametrize('dtype', [None, object])
def test_rank_2d_tie_methods(self, method, axis, dtype):
    df = self.df

    def _check2d(df, expected, method='average', axis=0):
        exp_df = DataFrame({'A': expected, 'B': expected})
        if axis == 1:
            df = df.T
            exp_df = exp_df.T
        result = df.rank(method=method, axis=axis)
        tm.assert_frame_equal(result, exp_df)
    disabled = {(object, 'first')}
    if (dtype, method) in disabled:
        return
    frame = df if dtype is None else df.astype(dtype)
    _check2d(frame, self.results[method], method=method, axis=axis)