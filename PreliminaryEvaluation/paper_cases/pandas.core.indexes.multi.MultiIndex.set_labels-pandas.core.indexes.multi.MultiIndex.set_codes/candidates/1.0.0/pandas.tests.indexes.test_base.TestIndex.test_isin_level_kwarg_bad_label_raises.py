@pytest.mark.parametrize('label', [1.0, 'foobar', 'xyzzy', np.nan])
def test_isin_level_kwarg_bad_label_raises(self, label, indices):
    index = indices
    if isinstance(index, MultiIndex):
        index = index.rename(['foo', 'bar'])
        msg = f"'Level {label} not found'"
    else:
        index = index.rename('foo')
        msg = f'Requested level \\({label}\\) does not match index name \\(foo\\)'
    with pytest.raises(KeyError, match=msg):
        index.isin([], level=label)