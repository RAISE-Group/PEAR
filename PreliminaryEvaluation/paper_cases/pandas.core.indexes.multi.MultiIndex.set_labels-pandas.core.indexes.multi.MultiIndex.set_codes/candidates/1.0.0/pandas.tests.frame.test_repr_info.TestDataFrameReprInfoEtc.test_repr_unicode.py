def test_repr_unicode(self):
    uval = 'σσσσ'
    bval = uval.encode('utf-8')
    df = DataFrame({'A': [uval, uval]})
    result = repr(df)
    ex_top = '      A'
    assert result.split('\n')[0].rstrip() == ex_top
    df = DataFrame({'A': [uval, uval]})
    result = repr(df)
    assert result.split('\n')[0].rstrip() == ex_top