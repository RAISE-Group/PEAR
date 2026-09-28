@pytest.mark.parametrize('cast_index', [True, False])
@pytest.mark.parametrize('vals', [Index(np.array([np_datetime64_compat('2011-01-01'), np_datetime64_compat('2011-01-02')])), Index([datetime(2011, 1, 1), datetime(2011, 1, 2)])])
def test_constructor_dtypes_to_datetime(self, cast_index, vals):
    if cast_index:
        index = Index(vals, dtype=object)
        assert isinstance(index, Index)
        assert index.dtype == object
    else:
        index = Index(vals)
        assert isinstance(index, DatetimeIndex)