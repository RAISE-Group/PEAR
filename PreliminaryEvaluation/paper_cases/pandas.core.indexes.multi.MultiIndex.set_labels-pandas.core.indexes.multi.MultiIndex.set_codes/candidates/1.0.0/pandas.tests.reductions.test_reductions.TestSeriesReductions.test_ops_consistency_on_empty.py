@pytest.mark.parametrize('method', ['mean', 'median', 'std', 'var'])
def test_ops_consistency_on_empty(self, method):
    result = getattr(Series(dtype=float), method)()
    assert pd.isna(result)
    tdser = Series([], dtype='m8[ns]')
    if method == 'var':
        with pytest.raises(TypeError, match="operation 'var' not allowed"):
            getattr(tdser, method)()
    else:
        result = getattr(tdser, method)()
        assert result is pd.NaT