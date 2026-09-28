def test_dti_custom_business_repr(self):
    repr(pd.bdate_range(datetime(2009, 1, 1), datetime(2010, 1, 1), freq='C'))