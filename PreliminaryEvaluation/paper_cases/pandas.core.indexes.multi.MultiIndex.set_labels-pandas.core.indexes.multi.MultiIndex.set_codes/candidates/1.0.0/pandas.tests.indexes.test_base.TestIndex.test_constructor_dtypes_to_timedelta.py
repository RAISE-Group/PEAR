@pytest.mark.parametrize('cast_index', [True, False])
@pytest.mark.parametrize('vals', [np.array([np.timedelta64(1, 'D'), np.timedelta64(1, 'D')]), [timedelta(1), timedelta(1)]])
def test_constructor_dtypes_to_timedelta(self, cast_index, vals):
    if cast_index:
        index = Index(vals, dtype=object)
        assert isinstance(index, Index)
        assert index.dtype == object
    else:
        index = Index(vals)
        assert isinstance(index, TimedeltaIndex)