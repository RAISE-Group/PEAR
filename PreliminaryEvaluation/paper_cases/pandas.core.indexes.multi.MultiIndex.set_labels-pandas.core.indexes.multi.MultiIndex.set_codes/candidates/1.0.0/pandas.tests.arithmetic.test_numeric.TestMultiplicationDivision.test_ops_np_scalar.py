@pytest.mark.parametrize('other', [np.nan, 7, -23, 2.718, -3.14, np.inf])
def test_ops_np_scalar(self, other):
    vals = np.random.randn(5, 3)
    f = lambda x: pd.DataFrame(x, index=list('ABCDE'), columns=['jim', 'joe', 'jolie'])
    df = f(vals)
    tm.assert_frame_equal(df / np.array(other), f(vals / other))
    tm.assert_frame_equal(np.array(other) * df, f(vals * other))
    tm.assert_frame_equal(df + np.array(other), f(vals + other))
    tm.assert_frame_equal(np.array(other) - df, f(other - vals))