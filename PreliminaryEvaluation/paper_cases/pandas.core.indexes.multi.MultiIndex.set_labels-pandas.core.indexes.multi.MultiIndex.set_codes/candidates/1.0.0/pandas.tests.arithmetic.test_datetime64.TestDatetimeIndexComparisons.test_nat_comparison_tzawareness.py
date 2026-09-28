@pytest.mark.parametrize('op', [operator.eq, operator.ne, operator.gt, operator.ge, operator.lt, operator.le])
def test_nat_comparison_tzawareness(self, op):
    dti = pd.DatetimeIndex(['2014-01-01', pd.NaT, '2014-03-01', pd.NaT, '2014-05-01', '2014-07-01'])
    expected = np.array([op == operator.ne] * len(dti))
    result = op(dti, pd.NaT)
    tm.assert_numpy_array_equal(result, expected)
    result = op(dti.tz_localize('US/Pacific'), pd.NaT)
    tm.assert_numpy_array_equal(result, expected)