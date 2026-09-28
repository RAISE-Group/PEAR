@pytest.mark.parametrize('holder', [pd.Int64Index, pd.UInt64Index, pd.Float64Index, pd.Series])
def test_ufunc_multiple_return_values(self, holder):
    obj = holder([1, 2, 3], name='x')
    box = pd.Series if holder is pd.Series else pd.Index
    result = np.modf(obj)
    assert isinstance(result, tuple)
    exp1 = pd.Float64Index([0.0, 0.0, 0.0], name='x')
    exp2 = pd.Float64Index([1.0, 2.0, 3.0], name='x')
    tm.assert_equal(result[0], tm.box_expected(exp1, box))
    tm.assert_equal(result[1], tm.box_expected(exp2, box))