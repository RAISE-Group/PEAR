def test_loc_setitem_with_existing_dst(self):
    start = pd.Timestamp('2017-10-29 00:00:00+0200', tz='Europe/Madrid')
    end = pd.Timestamp('2017-10-29 03:00:00+0100', tz='Europe/Madrid')
    ts = pd.Timestamp('2016-10-10 03:00:00', tz='Europe/Madrid')
    idx = pd.date_range(start, end, closed='left', freq='H')
    result = pd.DataFrame(index=idx, columns=['value'])
    result.loc[ts, 'value'] = 12
    expected = pd.DataFrame([np.nan] * len(idx) + [12], index=idx.append(pd.DatetimeIndex([ts])), columns=['value'], dtype=object)
    tm.assert_frame_equal(result, expected)