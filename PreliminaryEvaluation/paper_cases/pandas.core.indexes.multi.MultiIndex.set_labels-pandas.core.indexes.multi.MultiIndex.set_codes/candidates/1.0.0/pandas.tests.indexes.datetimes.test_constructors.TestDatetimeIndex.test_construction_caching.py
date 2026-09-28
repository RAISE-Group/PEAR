def test_construction_caching(self):
    df = pd.DataFrame({'dt': pd.date_range('20130101', periods=3), 'dttz': pd.date_range('20130101', periods=3, tz='US/Eastern'), 'dt_with_null': [pd.Timestamp('20130101'), pd.NaT, pd.Timestamp('20130103')], 'dtns': pd.date_range('20130101', periods=3, freq='ns')})
    assert df.dttz.dtype.tz.zone == 'US/Eastern'