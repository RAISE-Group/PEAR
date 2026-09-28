def test_to_numpy_alias(self):
    ts = Timestamp(datetime.now())
    assert ts.to_datetime64() == ts.to_numpy()