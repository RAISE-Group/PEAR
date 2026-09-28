def test_append_numpy_bug_1681(self):
    td = timedelta_range('1 days', '10 days', freq='2D')
    a = DataFrame()
    c = DataFrame({'A': 'foo', 'B': td}, index=td)
    str(c)
    result = a.append(c)
    assert (result['B'] == td).all()