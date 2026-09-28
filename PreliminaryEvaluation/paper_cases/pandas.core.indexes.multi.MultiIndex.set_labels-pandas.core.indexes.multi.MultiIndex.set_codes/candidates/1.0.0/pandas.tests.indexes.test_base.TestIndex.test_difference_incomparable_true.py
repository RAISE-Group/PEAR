@pytest.mark.xfail(reason='Not implemented')
@pytest.mark.parametrize('opname', ['difference', 'symmetric_difference'])
def test_difference_incomparable_true(self, opname):
    a = pd.Index([3, pd.Timestamp('2000'), 1])
    b = pd.Index([2, pd.Timestamp('1999'), 1])
    op = operator.methodcaller(opname, b, sort=True)
    with pytest.raises(TypeError, match='Cannot compare'):
        op(a)