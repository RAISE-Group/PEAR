def test_loc_duplicates(self):
    trange = pd.date_range(start=pd.Timestamp(year=2017, month=1, day=1), end=pd.Timestamp(year=2017, month=1, day=5))
    trange = trange.insert(loc=5, item=pd.Timestamp(year=2017, month=1, day=5))
    df = pd.DataFrame(0, index=trange, columns=['A', 'B'])
    bool_idx = np.array([False, False, False, False, False, True])
    df.loc[trange[bool_idx], 'A'] = 6
    expected = pd.DataFrame({'A': [0, 0, 0, 0, 6, 6], 'B': [0, 0, 0, 0, 0, 0]}, index=trange)
    tm.assert_frame_equal(df, expected)
    df = pd.DataFrame(0, index=trange, columns=['A', 'B'])
    df.loc[trange[bool_idx], 'A'] += 6
    tm.assert_frame_equal(df, expected)