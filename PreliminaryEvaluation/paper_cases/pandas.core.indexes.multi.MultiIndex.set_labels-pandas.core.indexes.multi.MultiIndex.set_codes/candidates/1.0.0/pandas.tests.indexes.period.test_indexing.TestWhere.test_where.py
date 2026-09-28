@pytest.mark.parametrize('klass', [list, tuple, np.array, Series])
def test_where(self, klass):
    i = period_range('20130101', periods=5, freq='D')
    cond = [True] * len(i)
    expected = i
    result = i.where(klass(cond))
    tm.assert_index_equal(result, expected)
    cond = [False] + [True] * (len(i) - 1)
    expected = PeriodIndex([pd.NaT] + i[1:].tolist(), freq='D')
    result = i.where(klass(cond))
    tm.assert_index_equal(result, expected)