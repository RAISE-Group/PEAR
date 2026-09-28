@pytest.mark.parametrize('box', [np.array, pd.Index])
def test_pi_sub_offset_array(self, box):
    pi = pd.PeriodIndex([pd.Period('2015Q1'), pd.Period('2016Q2')])
    other = box([pd.offsets.QuarterEnd(n=1, startingMonth=12), pd.offsets.QuarterEnd(n=-2, startingMonth=12)])
    expected = PeriodIndex([pi[n] - other[n] for n in range(len(pi))])
    with tm.assert_produces_warning(PerformanceWarning):
        res = pi - other
    tm.assert_index_equal(res, expected)
    anchored = box([pd.offsets.MonthEnd(), pd.offsets.Day(n=2)])
    with pytest.raises(IncompatibleFrequency):
        with tm.assert_produces_warning(PerformanceWarning):
            pi - anchored
    with pytest.raises(IncompatibleFrequency):
        with tm.assert_produces_warning(PerformanceWarning):
            anchored - pi