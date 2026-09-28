def test_dti_business_summary_pytz(self):
    pd.bdate_range('1/1/2005', '1/1/2009', tz=pytz.utc)._summary()