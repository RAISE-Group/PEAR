@pytest.mark.parametrize('dtype', [object, 'category'])
def test_api_per_dtype(self, index_or_series, dtype, any_skipna_inferred_dtype):
    box = index_or_series
    inferred_dtype, values = any_skipna_inferred_dtype
    t = box(values, dtype=dtype)
    if dtype == 'category' and inferred_dtype in ['period', 'interval']:
        pytest.xfail(reason='Conversion to numpy array fails because the ._values-attribute is not a numpy array for PeriodArray/IntervalArray; see GH 23553')
    types_passing_constructor = ['string', 'unicode', 'empty', 'bytes', 'mixed', 'mixed-integer']
    if inferred_dtype in types_passing_constructor:
        assert isinstance(t.str, strings.StringMethods)
    else:
        msg = 'Can only use .str accessor with string values.*'
        with pytest.raises(AttributeError, match=msg):
            t.str
        assert not hasattr(t, 'str')