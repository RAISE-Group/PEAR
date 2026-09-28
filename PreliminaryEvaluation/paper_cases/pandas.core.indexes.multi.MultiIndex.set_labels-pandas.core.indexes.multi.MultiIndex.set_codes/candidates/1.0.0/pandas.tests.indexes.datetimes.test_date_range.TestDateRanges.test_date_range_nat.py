def test_date_range_nat(self):
    msg = 'Neither `start` nor `end` can be NaT'
    with pytest.raises(ValueError, match=msg):
        date_range(start='2016-01-01', end=pd.NaT, freq='D')
    with pytest.raises(ValueError, match=msg):
        date_range(start=pd.NaT, end='2016-01-01', freq='D')