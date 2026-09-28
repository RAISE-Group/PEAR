@pytest.mark.parametrize('n', [1, 2, 3, 4])
@pytest.mark.parametrize('offset, kwd_name', [(pd.offsets.YearEnd, 'month'), (pd.offsets.QuarterEnd, 'startingMonth'), (pd.offsets.MonthEnd, None), (pd.offsets.Week, 'weekday')])
def test_sub_n_gt_1_offsets(self, offset, kwd_name, n):
    kwds = {kwd_name: 3} if kwd_name is not None else {}
    p1_d = '19910905'
    p2_d = '19920406'
    freq = offset(n, normalize=False, **kwds)
    p1 = pd.PeriodIndex([p1_d], freq=freq)
    p2 = pd.PeriodIndex([p2_d], freq=freq)
    result = p2 - p1
    expected = pd.PeriodIndex([p2_d], freq=freq.base) - pd.PeriodIndex([p1_d], freq=freq.base)
    tm.assert_index_equal(result, expected)