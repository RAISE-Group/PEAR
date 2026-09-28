def test_dti_repr_short(self):
    dr = pd.date_range(start='1/1/2012', periods=1)
    repr(dr)
    dr = pd.date_range(start='1/1/2012', periods=2)
    repr(dr)
    dr = pd.date_range(start='1/1/2012', periods=3)
    repr(dr)