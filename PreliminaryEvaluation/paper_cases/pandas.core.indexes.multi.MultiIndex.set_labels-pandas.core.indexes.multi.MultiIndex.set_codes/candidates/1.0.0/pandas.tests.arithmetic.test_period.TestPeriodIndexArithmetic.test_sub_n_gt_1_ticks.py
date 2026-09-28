@pytest.mark.parametrize('n', [1, 2, 3, 4])
def test_sub_n_gt_1_ticks(self, tick_classes, n):
    p1_d = '19910905'
    p2_d = '19920406'
    p1 = pd.PeriodIndex([p1_d], freq=tick_classes(n))
    p2 = pd.PeriodIndex([p2_d], freq=tick_classes(n))
    expected = pd.PeriodIndex([p2_d], freq=p2.freq.base) - pd.PeriodIndex([p1_d], freq=p1.freq.base)
    tm.assert_index_equal(p2 - p1, expected)