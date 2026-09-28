def test_loc_incremental_setitem_with_dst(self):
    base = datetime(2015, 11, 1, tzinfo=tz.gettz('US/Pacific'))
    idxs = [base + timedelta(seconds=i * 900) for i in range(16)]
    result = pd.Series([0], index=[idxs[0]])
    for ts in idxs:
        result.loc[ts] = 1
    expected = pd.Series(1, index=idxs)
    tm.assert_series_equal(result, expected)