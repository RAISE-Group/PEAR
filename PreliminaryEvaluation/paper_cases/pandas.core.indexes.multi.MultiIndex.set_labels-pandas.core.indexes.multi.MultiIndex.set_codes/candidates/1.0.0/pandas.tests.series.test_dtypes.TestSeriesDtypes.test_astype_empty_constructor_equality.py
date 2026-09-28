@pytest.mark.parametrize('dtype', np.typecodes['All'])
def test_astype_empty_constructor_equality(self, dtype):
    if dtype not in ('S', 'V', 'M', 'm'):
        init_empty = Series([], dtype=dtype)
        with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
            as_type_empty = Series([]).astype(dtype)
        tm.assert_series_equal(init_empty, as_type_empty)