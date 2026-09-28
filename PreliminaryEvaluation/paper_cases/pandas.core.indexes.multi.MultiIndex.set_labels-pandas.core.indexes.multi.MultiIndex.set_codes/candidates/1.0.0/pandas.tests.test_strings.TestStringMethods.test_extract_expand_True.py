def test_extract_expand_True(self):
    values = Series(['fooBAD__barBAD', np.nan, 'foo'])
    er = [np.nan, np.nan]
    result = values.str.extract('.*(BAD[_]+).*(BAD)', expand=True)
    exp = DataFrame([['BAD__', 'BAD'], er, er])
    tm.assert_frame_equal(result, exp)
    mixed = Series(['aBAD_BAD', np.nan, 'BAD_b_BAD', True, datetime.today(), 'foo', None, 1, 2.0])
    rs = Series(mixed).str.extract('.*(BAD[_]+).*(BAD)', expand=True)
    exp = DataFrame([['BAD_', 'BAD'], er, ['BAD_', 'BAD'], er, er, er, er, er, er])
    tm.assert_frame_equal(rs, exp)
    for klass in [Series, Index]:
        s_or_idx = klass(['A1', 'B2', 'C3'])
        msg = 'pattern contains no capture groups'
        with pytest.raises(ValueError, match=msg):
            s_or_idx.str.extract('[ABC][123]', expand=True)
        with pytest.raises(ValueError, match=msg):
            s_or_idx.str.extract('(?:[AB]).*', expand=True)
        s_or_idx = klass(['A1', 'A2'])
        result_df = s_or_idx.str.extract('(?P<uno>A)\\d', expand=True)
        assert isinstance(result_df, DataFrame)
        result_series = result_df['uno']
        tm.assert_series_equal(result_series, Series(['A', 'A'], name='uno'))