def test_hour(self):
    dr = date_range(start=Timestamp('2000-02-27'), periods=5, freq='H')
    r1 = pd.Index([x.to_julian_date() for x in dr])
    r2 = dr.to_julian_date()
    assert isinstance(r2, pd.Float64Index)
    tm.assert_index_equal(r1, r2)