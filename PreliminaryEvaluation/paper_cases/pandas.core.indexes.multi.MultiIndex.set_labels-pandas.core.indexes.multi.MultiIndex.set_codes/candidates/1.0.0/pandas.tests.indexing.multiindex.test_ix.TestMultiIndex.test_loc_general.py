def test_loc_general(self):
    data = {'amount': {0: 700, 1: 600, 2: 222, 3: 333, 4: 444}, 'col': {0: 3.5, 1: 3.5, 2: 4.0, 3: 4.0, 4: 4.0}, 'year': {0: 2012, 1: 2011, 2: 2012, 3: 2012, 4: 2012}}
    df = DataFrame(data).set_index(keys=['col', 'year'])
    key = (4.0, 2012)
    with tm.assert_produces_warning(PerformanceWarning):
        tm.assert_frame_equal(df.loc[key], df.iloc[2:])
    df.sort_index(inplace=True)
    res = df.loc[key]
    index = MultiIndex.from_arrays([[4.0] * 3, [2012] * 3], names=['col', 'year'])
    expected = DataFrame({'amount': [222, 333, 444]}, index=index)
    tm.assert_frame_equal(res, expected)