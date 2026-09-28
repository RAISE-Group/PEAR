def test_construction(self):
    msg = 'DatetimeTZDtype only supports ns units'
    with pytest.raises(ValueError, match=msg):
        DatetimeTZDtype('ms', 'US/Eastern')