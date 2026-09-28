@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_array_of_dt64s(self, cache):
    dts = [np.datetime64('2000-01-01'), np.datetime64('2000-01-02')]
    tm.assert_index_equal(pd.to_datetime(dts, cache=cache), pd.DatetimeIndex([Timestamp(x).asm8 for x in dts]))
    dts_with_oob = dts + [np.datetime64('9999-01-01')]
    msg = 'Out of bounds nanosecond timestamp: 9999-01-01 00:00:00'
    with pytest.raises(OutOfBoundsDatetime, match=msg):
        pd.to_datetime(dts_with_oob, errors='raise')
    tm.assert_index_equal(pd.to_datetime(dts_with_oob, errors='coerce', cache=cache), pd.DatetimeIndex([Timestamp(dts_with_oob[0]).asm8, Timestamp(dts_with_oob[1]).asm8, pd.NaT]))
    tm.assert_index_equal(pd.to_datetime(dts_with_oob, errors='ignore', cache=cache), pd.Index([dt.item() for dt in dts_with_oob]))