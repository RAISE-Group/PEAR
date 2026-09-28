def test_slice_year(self):
    dti = date_range(freq='B', start=datetime(2005, 1, 1), periods=500)
    s = Series(np.arange(len(dti)), index=dti)
    result = s['2005']
    expected = s[s.index.year == 2005]
    tm.assert_series_equal(result, expected)
    df = DataFrame(np.random.rand(len(dti), 5), index=dti)
    result = df.loc['2005']
    expected = df[df.index.year == 2005]
    tm.assert_frame_equal(result, expected)
    rng = date_range('1/1/2000', '1/1/2010')
    result = rng.get_loc('2009')
    expected = slice(3288, 3653)
    assert result == expected