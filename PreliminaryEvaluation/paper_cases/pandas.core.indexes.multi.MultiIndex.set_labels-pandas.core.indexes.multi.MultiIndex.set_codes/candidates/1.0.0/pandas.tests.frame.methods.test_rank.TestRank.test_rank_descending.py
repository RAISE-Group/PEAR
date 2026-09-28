@pytest.mark.parametrize('dtype', ['O', 'f8', 'i8'])
def test_rank_descending(self, method, dtype):
    if 'i' in dtype:
        df = self.df.dropna()
    else:
        df = self.df.astype(dtype)
    res = df.rank(ascending=False)
    expected = (df.max() - df).rank()
    tm.assert_frame_equal(res, expected)
    if method == 'first' and dtype == 'O':
        return
    expected = (df.max() - df).rank(method=method)
    if dtype != 'O':
        res2 = df.rank(method=method, ascending=False, numeric_only=True)
        tm.assert_frame_equal(res2, expected)
    res3 = df.rank(method=method, ascending=False, numeric_only=False)
    tm.assert_frame_equal(res3, expected)