@pytest.mark.parametrize('op', AGG_FUNCTIONS)
@pytest.mark.parametrize('level', [0, 1])
@pytest.mark.parametrize('skipna', [True, False])
@pytest.mark.parametrize('sort', [True, False])
def test_series_group_min_max(self, op, level, skipna, sort):
    grouped = self.series.groupby(level=level, sort=sort)
    leftside = grouped.agg(lambda x: getattr(x, op)(skipna=skipna))
    rightside = getattr(self.series, op)(level=level, skipna=skipna)
    if sort:
        rightside = rightside.sort_index(level=level)
    tm.assert_series_equal(leftside, rightside)