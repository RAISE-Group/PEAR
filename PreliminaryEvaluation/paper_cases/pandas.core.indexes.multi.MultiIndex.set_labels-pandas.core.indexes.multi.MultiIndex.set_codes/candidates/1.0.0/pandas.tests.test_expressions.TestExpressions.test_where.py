@pytest.mark.parametrize('cond', [True, False])
@pytest.mark.parametrize('df', [_frame, _frame2, _mixed, _mixed2])
def test_where(self, cond, df):

    def testit():
        c = np.empty(df.shape, dtype=np.bool_)
        c.fill(cond)
        result = expr.where(c, df.values, df.values + 1)
        expected = np.where(c, df.values, df.values + 1)
        tm.assert_numpy_array_equal(result, expected)
    expr.set_use_numexpr(False)
    testit()
    expr.set_use_numexpr(True)
    expr.set_numexpr_threads(1)
    testit()
    expr.set_numexpr_threads()
    testit()