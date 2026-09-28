def test_alias_to_unit_bad_alias_raises(self):
    with pytest.raises(TypeError, match=''):
        DatetimeTZDtype('this is a bad string')
    with pytest.raises(TypeError, match=''):
        DatetimeTZDtype('datetime64[ns, US/NotATZ]')