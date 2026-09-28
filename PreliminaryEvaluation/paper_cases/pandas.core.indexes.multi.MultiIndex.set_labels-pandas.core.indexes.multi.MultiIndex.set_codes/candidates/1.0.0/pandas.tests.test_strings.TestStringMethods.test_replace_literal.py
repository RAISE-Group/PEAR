def test_replace_literal(self):
    values = Series(['f.o', 'foo', np.nan])
    exp = Series(['bao', 'bao', np.nan])
    result = values.str.replace('f.', 'ba')
    tm.assert_series_equal(result, exp)
    exp = Series(['bao', 'foo', np.nan])
    result = values.str.replace('f.', 'ba', regex=False)
    tm.assert_series_equal(result, exp)
    callable_repl = lambda m: m.group(0).swapcase()
    compiled_pat = re.compile('[a-z][A-Z]{2}')
    msg = 'Cannot use a callable replacement when regex=False'
    with pytest.raises(ValueError, match=msg):
        values.str.replace('abc', callable_repl, regex=False)
    msg = 'Cannot use a compiled regex as replacement pattern with regex=False'
    with pytest.raises(ValueError, match=msg):
        values.str.replace(compiled_pat, '', regex=False)