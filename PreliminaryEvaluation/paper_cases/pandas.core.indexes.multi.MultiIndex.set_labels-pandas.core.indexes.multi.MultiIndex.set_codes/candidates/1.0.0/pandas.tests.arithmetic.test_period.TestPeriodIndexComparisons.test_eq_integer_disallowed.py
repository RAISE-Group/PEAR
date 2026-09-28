@pytest.mark.parametrize('other', [2017, [2017, 2017, 2017], np.array([2017, 2017, 2017]), np.array([2017, 2017, 2017], dtype=object), pd.Index([2017, 2017, 2017])])
def test_eq_integer_disallowed(self, other):
    idx = PeriodIndex(['2017', '2017', '2018'], freq='D')
    expected = np.array([False, False, False])
    result = idx == other
    tm.assert_numpy_array_equal(result, expected)
    with pytest.raises(TypeError):
        idx < other
    with pytest.raises(TypeError):
        idx > other
    with pytest.raises(TypeError):
        idx <= other
    with pytest.raises(TypeError):
        idx >= other