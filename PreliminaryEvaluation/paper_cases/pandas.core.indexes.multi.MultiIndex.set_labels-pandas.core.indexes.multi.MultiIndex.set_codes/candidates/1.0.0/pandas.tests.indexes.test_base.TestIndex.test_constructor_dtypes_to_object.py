@pytest.mark.parametrize('cast_index', [True, False])
@pytest.mark.parametrize('vals', [[True, False, True], np.array([True, False, True], dtype=bool)])
def test_constructor_dtypes_to_object(self, cast_index, vals):
    if cast_index:
        index = Index(vals, dtype=bool)
    else:
        index = Index(vals)
    assert isinstance(index, Index)
    assert index.dtype == object