def test_identity(self):
    td = Timedelta(10, unit='d')
    assert isinstance(td, Timedelta)
    assert isinstance(td, timedelta)