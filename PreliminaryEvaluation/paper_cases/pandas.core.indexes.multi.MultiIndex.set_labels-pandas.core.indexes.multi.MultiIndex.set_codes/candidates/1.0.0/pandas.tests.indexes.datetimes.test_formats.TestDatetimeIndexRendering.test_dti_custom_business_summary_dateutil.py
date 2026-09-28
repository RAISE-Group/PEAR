def test_dti_custom_business_summary_dateutil(self):
    pd.bdate_range('1/1/2005', '1/1/2009', freq='C', tz=dateutil.tz.tzutc())._summary()