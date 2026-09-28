@pytest.mark.parametrize('dtype', [object, 'category'])
def test_api_per_method(self, index_or_series, dtype, any_allowed_skipna_inferred_dtype, any_string_method):
    box = index_or_series
    inferred_dtype, values = any_allowed_skipna_inferred_dtype
    method_name, args, kwargs = any_string_method
    if method_name in ['partition', 'rpartition'] and box == Index and (inferred_dtype == 'empty'):
        pytest.xfail(reason='Method cannot deal with empty Index')
    if method_name == 'split' and box == Index and (values.size == 0) and (kwargs.get('expand', None) is not None):
        pytest.xfail(reason='Split fails on empty Series when expand=True')
    if method_name == 'get_dummies' and box == Index and (inferred_dtype == 'empty') and (dtype == object or values.size == 0):
        pytest.xfail(reason='Need to fortify get_dummies corner cases')
    t = box(values, dtype=dtype)
    method = getattr(t.str, method_name)
    bytes_allowed = method_name in ['decode', 'get', 'len', 'slice']
    mixed_allowed = method_name not in ['cat']
    allowed_types = ['string', 'unicode', 'empty'] + ['bytes'] * bytes_allowed + ['mixed', 'mixed-integer'] * mixed_allowed
    if inferred_dtype in allowed_types:
        method(*args, **kwargs)
    else:
        msg = f'Cannot use .str.{method_name} with values of inferred dtype {repr(inferred_dtype)}.'
        with pytest.raises(TypeError, match=msg):
            method(*args, **kwargs)