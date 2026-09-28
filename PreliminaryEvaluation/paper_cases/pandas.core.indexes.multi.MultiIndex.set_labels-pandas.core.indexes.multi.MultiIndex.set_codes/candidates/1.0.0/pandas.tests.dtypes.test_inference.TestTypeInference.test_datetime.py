def test_datetime(self):
    dates = [datetime(2012, 1, x) for x in range(1, 20)]
    index = Index(dates)
    assert index.inferred_type == 'datetime64'