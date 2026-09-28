@pytest.mark.parametrize('box', [np.array, pd.Index])
def test_pi_add_offset_array(self, box):
    pi = pd.PeriodIndex([pd.Period('2015Q1'), pd.Period('2016Q2')])
    offs = box([pd.offsets.QuarterEnd(n=1, startingMonth=12), pd.offsets.QuarterEnd(n=-2, startingMonth=12)])
    expected = pd.PeriodIndex([pd.Period('2015Q2'), pd.Period('2015Q4')])
    with tm.assert_produces_warning(PerformanceWarning):
        res = pi + offs
    tm.assert_index_equal(res, expected)
    with tm.assert_produces_warning(PerformanceWarning):
        res2 = offs + pi
    tm.assert_index_equal(res2, expected)
    unanchored = np.array([pd.offsets.Hour(n=1), pd.offsets.Minute(n=-2)])
    with pytest.raises(IncompatibleFrequency):
        with tm.assert_produces_warning(PerformanceWarning):
            pi + unanchored
    with pytest.raises(IncompatibleFrequency):
        with tm.assert_produces_warning(PerformanceWarning):
            unanchored + pi