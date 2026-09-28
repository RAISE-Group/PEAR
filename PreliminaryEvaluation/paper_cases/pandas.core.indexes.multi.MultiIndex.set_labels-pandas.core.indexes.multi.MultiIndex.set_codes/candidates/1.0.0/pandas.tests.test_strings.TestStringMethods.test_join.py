def test_join(self):
    values = Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
    result = values.str.split('_').str.join('_')
    tm.assert_series_equal(values, result)
    mixed = Series(['a_b', np.nan, 'asdf_cas_asdf', True, datetime.today(), 'foo', None, 1, 2.0])
    rs = Series(mixed).str.split('_').str.join('_')
    xp = Series(['a_b', np.nan, 'asdf_cas_asdf', np.nan, np.nan, 'foo', np.nan, np.nan, np.nan])
    assert isinstance(rs, Series)
    tm.assert_almost_equal(rs, xp)