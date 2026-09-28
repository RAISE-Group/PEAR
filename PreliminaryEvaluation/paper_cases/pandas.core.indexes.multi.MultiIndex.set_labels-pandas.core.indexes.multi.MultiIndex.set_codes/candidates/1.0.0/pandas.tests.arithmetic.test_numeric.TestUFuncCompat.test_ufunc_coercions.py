@pytest.mark.parametrize('holder', [pd.Int64Index, pd.UInt64Index, pd.Float64Index, pd.Series])
def test_ufunc_coercions(self, holder):
    idx = holder([1, 2, 3, 4, 5], name='x')
    box = pd.Series if holder is pd.Series else pd.Index
    result = np.sqrt(idx)
    assert result.dtype == 'f8' and isinstance(result, box)
    exp = pd.Float64Index(np.sqrt(np.array([1, 2, 3, 4, 5])), name='x')
    exp = tm.box_expected(exp, box)
    tm.assert_equal(result, exp)
    result = np.divide(idx, 2.0)
    assert result.dtype == 'f8' and isinstance(result, box)
    exp = pd.Float64Index([0.5, 1.0, 1.5, 2.0, 2.5], name='x')
    exp = tm.box_expected(exp, box)
    tm.assert_equal(result, exp)
    result = idx + 2.0
    assert result.dtype == 'f8' and isinstance(result, box)
    exp = pd.Float64Index([3.0, 4.0, 5.0, 6.0, 7.0], name='x')
    exp = tm.box_expected(exp, box)
    tm.assert_equal(result, exp)
    result = idx - 2.0
    assert result.dtype == 'f8' and isinstance(result, box)
    exp = pd.Float64Index([-1.0, 0.0, 1.0, 2.0, 3.0], name='x')
    exp = tm.box_expected(exp, box)
    tm.assert_equal(result, exp)
    result = idx * 1.0
    assert result.dtype == 'f8' and isinstance(result, box)
    exp = pd.Float64Index([1.0, 2.0, 3.0, 4.0, 5.0], name='x')
    exp = tm.box_expected(exp, box)
    tm.assert_equal(result, exp)
    result = idx / 2.0
    assert result.dtype == 'f8' and isinstance(result, box)
    exp = pd.Float64Index([0.5, 1.0, 1.5, 2.0, 2.5], name='x')
    exp = tm.box_expected(exp, box)
    tm.assert_equal(result, exp)