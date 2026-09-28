@pytest.mark.parametrize('opname', ['difference', 'symmetric_difference'])
def test_difference_incomparable(self, opname):
    a = pd.Index([3, pd.Timestamp('2000'), 1])
    b = pd.Index([2, pd.Timestamp('1999'), 1])
    op = operator.methodcaller(opname, b)
    result = op(a)
    expected = pd.Index([3, pd.Timestamp('2000'), 2, pd.Timestamp('1999')])
    if opname == 'difference':
        expected = expected[:2]
    tm.assert_index_equal(result, expected)
    op = operator.methodcaller(opname, b, sort=False)
    result = op(a)
    tm.assert_index_equal(result, expected)