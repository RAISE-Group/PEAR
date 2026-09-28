def test_constructor_wrong_precision_raises(self):
    with pytest.raises(ValueError):
        pd.DatetimeIndex(['2000'], dtype='datetime64[us]')