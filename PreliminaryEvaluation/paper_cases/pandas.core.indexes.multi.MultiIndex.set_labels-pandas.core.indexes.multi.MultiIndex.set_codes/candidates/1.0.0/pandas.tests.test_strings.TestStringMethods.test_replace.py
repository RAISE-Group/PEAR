def test_replace(self):
    values = Series(['fooBAD__barBAD', np.nan])
    result = values.str.replace('BAD[_]*', '')
    exp = Series(['foobar', np.nan])
    tm.assert_series_equal(result, exp)
    result = values.str.replace('BAD[_]*', '', n=1)
    exp = Series(['foobarBAD', np.nan])
    tm.assert_series_equal(result, exp)
    mixed = Series(['aBAD', np.nan, 'bBAD', True, datetime.today(), 'fooBAD', None, 1, 2.0])
    rs = Series(mixed).str.replace('BAD[_]*', '')
    xp = Series(['a', np.nan, 'b', np.nan, np.nan, 'foo', np.nan, np.nan, np.nan])
    assert isinstance(rs, Series)
    tm.assert_almost_equal(rs, xp)
    values = Series([b'abcd,\xc3\xa0'.decode('utf-8')])
    exp = Series([b'abcd, \xc3\xa0'.decode('utf-8')])
    result = values.str.replace('(?<=\\w),(?=\\w)', ', ', flags=re.UNICODE)
    tm.assert_series_equal(result, exp)
    msg = 'repl must be a string or callable'
    for klass in (Series, Index):
        for repl in (None, 3, {'a': 'b'}):
            for data in (['a', 'b', None], ['a', 'b', 'c', 'ad']):
                values = klass(data)
                with pytest.raises(TypeError, match=msg):
                    values.str.replace('a', repl)