def test_constructor_no_precision_raises(self):
    msg = 'with no precision is not allowed'
    with pytest.raises(ValueError, match=msg):
        pd.TimedeltaIndex(['2000'], dtype='timedelta64')
    with pytest.raises(ValueError, match=msg):
        pd.Index(['2000'], dtype='timedelta64')