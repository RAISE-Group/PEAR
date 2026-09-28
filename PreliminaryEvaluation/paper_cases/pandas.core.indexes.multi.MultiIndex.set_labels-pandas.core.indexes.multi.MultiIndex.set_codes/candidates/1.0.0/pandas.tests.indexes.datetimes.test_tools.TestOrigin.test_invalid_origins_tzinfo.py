def test_invalid_origins_tzinfo(self):
    with pytest.raises(ValueError):
        pd.to_datetime(1, unit='D', origin=datetime(2000, 1, 1, tzinfo=pytz.utc))