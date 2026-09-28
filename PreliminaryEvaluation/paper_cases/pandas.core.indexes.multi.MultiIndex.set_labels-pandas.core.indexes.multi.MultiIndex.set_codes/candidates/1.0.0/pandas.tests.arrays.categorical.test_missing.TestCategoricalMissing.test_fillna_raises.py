@pytest.mark.parametrize('fillna_kwargs, msg', [(dict(value=1, method='ffill'), "Cannot specify both 'value' and 'method'."), (dict(), "Must specify a fill 'value' or 'method'."), (dict(method='bad'), 'Invalid fill method. Expecting .* bad'), (dict(value=Series([1, 2, 3, 4, 'a'])), 'fill value must be in categories')])
def test_fillna_raises(self, fillna_kwargs, msg):
    cat = Categorical([1, 2, 3, None, None])
    with pytest.raises(ValueError, match=msg):
        cat.fillna(**fillna_kwargs)