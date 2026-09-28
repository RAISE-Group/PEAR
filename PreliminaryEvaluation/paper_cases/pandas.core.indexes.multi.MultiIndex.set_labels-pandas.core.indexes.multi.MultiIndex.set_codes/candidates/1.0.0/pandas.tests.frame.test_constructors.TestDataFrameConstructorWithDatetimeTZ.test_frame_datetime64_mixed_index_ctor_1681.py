def test_frame_datetime64_mixed_index_ctor_1681(self):
    dr = date_range('2011/1/1', '2012/1/1', freq='W-FRI')
    ts = Series(dr)
    d = DataFrame({'A': 'foo', 'B': ts}, index=dr)
    assert d['B'].isna().all()