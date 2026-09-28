def test_extract_expand_False(self):
    values = Series(['fooBAD__barBAD', np.nan, 'foo'])
    er = [np.nan, np.nan]
    result = values.str.extract('.*(BAD[_]+).*(BAD)', expand=False)
    exp = DataFrame([['BAD__', 'BAD'], er, er])
    tm.assert_frame_equal(result, exp)
    mixed = Series(['aBAD_BAD', np.nan, 'BAD_b_BAD', True, datetime.today(), 'foo', None, 1, 2.0])
    rs = Series(mixed).str.extract('.*(BAD[_]+).*(BAD)', expand=False)
    exp = DataFrame([['BAD_', 'BAD'], er, ['BAD_', 'BAD'], er, er, er, er, er, er])
    tm.assert_frame_equal(rs, exp)
    values = Series(['fooBAD__barBAD', np.nan, 'foo'])
    result = values.str.extract('.*(BAD[_]+).*(BAD)', expand=False)
    exp = DataFrame([['BAD__', 'BAD'], er, er])
    tm.assert_frame_equal(result, exp)
    idx = Index(['A1', 'A2', 'A3', 'A4', 'B5'])
    with pytest.raises(ValueError, match='supported'):
        idx.str.extract('([AB])([123])', expand=False)
    for klass in [Series, Index]:
        s_or_idx = klass(['A1', 'B2', 'C3'])
        msg = 'pattern contains no capture groups'
        with pytest.raises(ValueError, match=msg):
            s_or_idx.str.extract('[ABC][123]', expand=False)
        with pytest.raises(ValueError, match=msg):
            s_or_idx.str.extract('(?:[AB]).*', expand=False)
        s_or_idx = klass(['A1', 'A2'])
        result = s_or_idx.str.extract('(?P<uno>A)\\d', expand=False)
        assert result.name == 'uno'
        exp = klass(['A', 'A'], name='uno')
        if klass == Series:
            tm.assert_series_equal(result, exp)
        else:
            tm.assert_index_equal(result, exp)
    s = Series(['A1', 'B2', 'C3'])
    result = s.str.extract('(_)', expand=False)
    exp = Series([np.nan, np.nan, np.nan], dtype=object)
    tm.assert_series_equal(result, exp)
    result = s.str.extract('(_)(_)', expand=False)
    exp = DataFrame([[np.nan, np.nan], [np.nan, np.nan], [np.nan, np.nan]], dtype=object)
    tm.assert_frame_equal(result, exp)
    result = s.str.extract('([AB])[123]', expand=False)
    exp = Series(['A', 'B', np.nan])
    tm.assert_series_equal(result, exp)
    result = s.str.extract('([AB])([123])', expand=False)
    exp = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]])
    tm.assert_frame_equal(result, exp)
    result = s.str.extract('(?P<letter>[AB])', expand=False)
    exp = Series(['A', 'B', np.nan], name='letter')
    tm.assert_series_equal(result, exp)
    result = s.str.extract('(?P<letter>[AB])(?P<number>[123])', expand=False)
    exp = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], columns=['letter', 'number'])
    tm.assert_frame_equal(result, exp)
    result = s.str.extract('([AB])(?P<number>[123])', expand=False)
    exp = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]], columns=[0, 'number'])
    tm.assert_frame_equal(result, exp)
    result = s.str.extract('([AB])(?:[123])', expand=False)
    exp = Series(['A', 'B', np.nan])
    tm.assert_series_equal(result, exp)
    result = Series(['A11', 'B22', 'C33']).str.extract('([AB])([123])(?:[123])', expand=False)
    exp = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]])
    tm.assert_frame_equal(result, exp)
    result = Series(['A1', 'B2', '3']).str.extract('(?P<letter>[AB])?(?P<number>[123])', expand=False)
    exp = DataFrame([['A', '1'], ['B', '2'], [np.nan, '3']], columns=['letter', 'number'])
    tm.assert_frame_equal(result, exp)
    result = Series(['A1', 'B2', 'C']).str.extract('(?P<letter>[ABC])(?P<number>[123])?', expand=False)
    exp = DataFrame([['A', '1'], ['B', '2'], ['C', np.nan]], columns=['letter', 'number'])
    tm.assert_frame_equal(result, exp)

    def check_index(index):
        data = ['A1', 'B2', 'C']
        index = index[:len(data)]
        s = Series(data, index=index)
        result = s.str.extract('(\\d)', expand=False)
        exp = Series(['1', '2', np.nan], index=index)
        tm.assert_series_equal(result, exp)
        result = Series(data, index=index).str.extract('(?P<letter>\\D)(?P<number>\\d)?', expand=False)
        e_list = [['A', '1'], ['B', '2'], ['C', np.nan]]
        exp = DataFrame(e_list, columns=['letter', 'number'], index=index)
        tm.assert_frame_equal(result, exp)
    i_funs = [tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeIntIndex, tm.makeDateIndex, tm.makePeriodIndex, tm.makeRangeIndex]
    for index in i_funs:
        check_index(index())
    s = Series(['a3', 'b3', 'c2'], name='bob')
    r = s.str.extract('(?P<sue>[a-z])', expand=False)
    e = Series(['a', 'b', 'c'], name='sue')
    tm.assert_series_equal(r, e)
    assert r.name == e.name