def test_as_array_datetime_tz(self):
    mgr = create_mgr('h: M8[ns, US/Eastern]; g: M8[ns, CET]')
    assert mgr.get('h').dtype == 'datetime64[ns, US/Eastern]'
    assert mgr.get('g').dtype == 'datetime64[ns, CET]'
    assert mgr.as_array().dtype == 'object'