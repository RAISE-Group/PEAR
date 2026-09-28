def test_rename_axis_supported(self):
    s = Series(range(5))
    s.rename({}, axis=0)
    s.rename({}, axis='index')