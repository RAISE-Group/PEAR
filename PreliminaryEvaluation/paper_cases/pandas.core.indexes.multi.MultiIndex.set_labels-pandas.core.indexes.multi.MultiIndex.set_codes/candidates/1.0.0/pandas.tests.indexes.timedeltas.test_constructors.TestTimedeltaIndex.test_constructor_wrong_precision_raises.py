def test_constructor_wrong_precision_raises(self):
    with pytest.raises(ValueError):
        pd.TimedeltaIndex(['2000'], dtype='timedelta64[us]')