def test_dti_tz_localize_bdate_range(self):
    dr = pd.bdate_range('1/1/2009', '1/1/2010')
    dr_utc = pd.bdate_range('1/1/2009', '1/1/2010', tz=pytz.utc)
    localized = dr.tz_localize(pytz.utc)
    tm.assert_index_equal(dr_utc, localized)