@pytest.mark.parametrize('dtype, rdtype', dtypes + [('object', int), ('category', int)])
@pytest.mark.filterwarnings('ignore:\\n    Passing:FutureWarning')
def test_iterable_map(self, index_or_series, dtype, rdtype):
    typ = index_or_series
    s = typ([1], dtype=dtype)
    result = s.map(type)[0]
    if not isinstance(rdtype, tuple):
        rdtype = tuple([rdtype])
    assert result in rdtype