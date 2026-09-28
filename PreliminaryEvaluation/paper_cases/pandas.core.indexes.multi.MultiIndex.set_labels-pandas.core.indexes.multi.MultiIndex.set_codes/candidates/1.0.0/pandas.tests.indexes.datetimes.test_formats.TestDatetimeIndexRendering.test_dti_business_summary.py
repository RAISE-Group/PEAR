def test_dti_business_summary(self):
    rng = pd.bdate_range(datetime(2009, 1, 1), datetime(2010, 1, 1))
    rng._summary()
    rng[2:2]._summary()