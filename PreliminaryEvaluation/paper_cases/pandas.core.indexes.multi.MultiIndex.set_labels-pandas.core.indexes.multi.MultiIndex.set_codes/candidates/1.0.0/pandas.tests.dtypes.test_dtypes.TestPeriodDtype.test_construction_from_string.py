def test_construction_from_string(self):
    result = PeriodDtype('period[D]')
    assert is_dtype_equal(self.dtype, result)
    result = PeriodDtype.construct_from_string('period[D]')
    assert is_dtype_equal(self.dtype, result)
    with pytest.raises(TypeError):
        PeriodDtype.construct_from_string('foo')
    with pytest.raises(TypeError):
        PeriodDtype.construct_from_string('period[foo]')
    with pytest.raises(TypeError):
        PeriodDtype.construct_from_string('foo[D]')
    with pytest.raises(TypeError):
        PeriodDtype.construct_from_string('datetime64[ns]')
    with pytest.raises(TypeError):
        PeriodDtype.construct_from_string('datetime64[ns, US/Eastern]')
    with pytest.raises(TypeError, match='list'):
        PeriodDtype.construct_from_string([1, 2, 3])