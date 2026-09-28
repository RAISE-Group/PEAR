@pytest.mark.parametrize('op', AGG_FUNCTIONS)
@pytest.mark.parametrize('level', [0, 1])
@pytest.mark.parametrize('axis', [0, 1])
@pytest.mark.parametrize('skipna', [True, False])
@pytest.mark.parametrize('sort', [True, False])
def test_frame_group_ops(self, op, level, axis, skipna, sort):
    self.frame.iloc[1, [1, 2]] = np.nan
    self.frame.iloc[7, [0, 1]] = np.nan
    level_name = self.frame.index.names[level]
    if axis == 0:
        frame = self.frame
    else:
        frame = self.frame.T
    grouped = frame.groupby(level=level, axis=axis, sort=sort)
    pieces = []

    def aggf(x):
        pieces.append(x)
        return getattr(x, op)(skipna=skipna, axis=axis)
    leftside = grouped.agg(aggf)
    rightside = getattr(frame, op)(level=level, axis=axis, skipna=skipna)
    if sort:
        rightside = rightside.sort_index(level=level, axis=axis)
        frame = frame.sort_index(level=level, axis=axis)
    level_index = frame._get_axis(axis).levels[level].rename(level_name)
    tm.assert_index_equal(leftside._get_axis(axis), level_index)
    tm.assert_index_equal(rightside._get_axis(axis), level_index)
    tm.assert_frame_equal(leftside, rightside)