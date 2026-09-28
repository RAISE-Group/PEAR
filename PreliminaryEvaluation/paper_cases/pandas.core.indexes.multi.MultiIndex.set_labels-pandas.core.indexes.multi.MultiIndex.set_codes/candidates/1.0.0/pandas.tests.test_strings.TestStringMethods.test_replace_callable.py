def test_replace_callable(self):
    values = Series(['fooBAD__barBAD', np.nan])
    repl = lambda m: m.group(0).swapcase()
    result = values.str.replace('[a-z][A-Z]{2}', repl, n=2)
    exp = Series(['foObaD__baRbaD', np.nan])
    tm.assert_series_equal(result, exp)
    p_err = '((takes)|(missing)) (?(2)from \\d+ to )?\\d+ (?(3)required )positional arguments?'
    repl = lambda: None
    with pytest.raises(TypeError, match=p_err):
        values.str.replace('a', repl)
    repl = lambda m, x: None
    with pytest.raises(TypeError, match=p_err):
        values.str.replace('a', repl)
    repl = lambda m, x, y=None: None
    with pytest.raises(TypeError, match=p_err):
        values.str.replace('a', repl)
    values = Series(['Foo Bar Baz', np.nan])
    pat = '(?P<first>\\w+) (?P<middle>\\w+) (?P<last>\\w+)'
    repl = lambda m: m.group('middle').swapcase()
    result = values.str.replace(pat, repl)
    exp = Series(['bAR', np.nan])
    tm.assert_series_equal(result, exp)