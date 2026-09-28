def test_setitem_cache_updating(self):
    cont = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    for do_ref in [False, False]:
        df = DataFrame({'a': cont, 'b': cont[3:] + cont[:3], 'c': np.arange(7)})
        if do_ref:
            df.loc[0, 'c']
        df.loc[7, 'c'] = 1
        assert df.loc[0, 'c'] == 0.0
        assert df.loc[7, 'c'] == 1.0
    expected = DataFrame({'A': [600, 600, 600]}, index=date_range('5/7/2014', '5/9/2014'))
    out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
    df = DataFrame({'C': ['A', 'A', 'A'], 'D': [100, 200, 300]})
    six = Timestamp('5/7/2014')
    eix = Timestamp('5/9/2014')
    for ix, row in df.iterrows():
        out.loc[six:eix, row['C']] = out.loc[six:eix, row['C']] + row['D']
    tm.assert_frame_equal(out, expected)
    tm.assert_series_equal(out['A'], expected['A'])
    out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
    for ix, row in df.iterrows():
        v = out[row['C']][six:eix] + row['D']
        out[row['C']][six:eix] = v
    tm.assert_frame_equal(out, expected)
    tm.assert_series_equal(out['A'], expected['A'])
    out = DataFrame({'A': [0, 0, 0]}, index=date_range('5/7/2014', '5/9/2014'))
    for ix, row in df.iterrows():
        out.loc[six:eix, row['C']] += row['D']
    tm.assert_frame_equal(out, expected)
    tm.assert_series_equal(out['A'], expected['A'])