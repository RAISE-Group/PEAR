def test_alias_to_unit_raises(self):
    with pytest.raises(ValueError, match='Passing a dtype alias'):
        DatetimeTZDtype('datetime64[ns, US/Central]')