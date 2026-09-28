def test_append_numpy_bug_1681(self):
    dr = date_range('2011/1/1', '2012/1/1', freq='W-FRI')
    a = DataFrame()
    c = DataFrame({'A': 'foo', 'B': dr}, index=dr)
    result = a.append(c)
    assert (result['B'] == dr).all()