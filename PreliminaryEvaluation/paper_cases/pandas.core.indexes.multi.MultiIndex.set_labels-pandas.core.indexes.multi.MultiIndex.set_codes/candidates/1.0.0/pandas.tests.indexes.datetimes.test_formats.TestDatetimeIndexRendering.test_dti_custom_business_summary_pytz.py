def test_dti_custom_business_summary_pytz(self):
    pd.bdate_range('1/1/2005', '1/1/2009', freq='C', tz=pytz.utc)._summary()