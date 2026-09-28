def test_constructor_strptime(self):
    fmt = '%Y%m%d-%H%M%S-%f%z'
    ts = '20190129-235348-000001+0000'
    with pytest.raises(NotImplementedError):
        Timestamp.strptime(ts, fmt)