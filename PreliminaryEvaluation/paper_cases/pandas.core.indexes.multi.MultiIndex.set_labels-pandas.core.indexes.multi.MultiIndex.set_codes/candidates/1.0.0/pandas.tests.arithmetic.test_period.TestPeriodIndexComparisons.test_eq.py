@pytest.mark.parametrize('other', ['2017', pd.Period('2017', freq='D')])
def test_eq(self, other):
    idx = PeriodIndex(['2017', '2017', '2018'], freq='D')
    expected = np.array([True, True, False])
    result = idx == other
    tm.assert_numpy_array_equal(result, expected)