@pytest.mark.parametrize('method', ['any', 'all'])
def test_any_all_level_axis_none_raises(self, method):
    df = DataFrame({'A': 1}, index=MultiIndex.from_product([['A', 'B'], ['a', 'b']], names=['out', 'in']))
    xpr = "Must specify 'axis' when aggregating by level."
    with pytest.raises(ValueError, match=xpr):
        getattr(df, method)(axis=None, level='out')