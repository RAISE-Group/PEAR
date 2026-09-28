def test_indexing_sliced(self):
    s = tm.SubclassedSeries([1, 2, 3, 4], index=list('abcd'))
    res = s.loc[['a', 'b']]
    exp = tm.SubclassedSeries([1, 2], index=list('ab'))
    tm.assert_series_equal(res, exp)
    res = s.iloc[[2, 3]]
    exp = tm.SubclassedSeries([3, 4], index=list('cd'))
    tm.assert_series_equal(res, exp)
    res = s.loc[['a', 'b']]
    exp = tm.SubclassedSeries([1, 2], index=list('ab'))
    tm.assert_series_equal(res, exp)