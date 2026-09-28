def test_as_array_datetime(self):
    mgr = create_mgr('h: datetime-1; g: datetime-2')
    assert mgr.as_array().dtype == 'M8[ns]'