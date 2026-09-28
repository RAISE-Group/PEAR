def test_datetimeindex_sub_datetimeindex_overflow(self):
    dtimax = pd.to_datetime(['now', pd.Timestamp.max])
    dtimin = pd.to_datetime(['now', pd.Timestamp.min])
    ts_neg = pd.to_datetime(['1950-01-01', '1950-01-01'])
    ts_pos = pd.to_datetime(['1980-01-01', '1980-01-01'])
    expected = pd.Timestamp.max.value - ts_pos[1].value
    result = dtimax - ts_pos
    assert result[1].value == expected
    expected = pd.Timestamp.min.value - ts_neg[1].value
    result = dtimin - ts_neg
    assert result[1].value == expected
    msg = 'Overflow in int64 addition'
    with pytest.raises(OverflowError, match=msg):
        dtimax - ts_neg
    with pytest.raises(OverflowError, match=msg):
        dtimin - ts_pos
    tmin = pd.to_datetime([pd.Timestamp.min])
    t1 = tmin + pd.Timedelta.max + pd.Timedelta('1us')
    with pytest.raises(OverflowError, match=msg):
        t1 - tmin
    tmax = pd.to_datetime([pd.Timestamp.max])
    t2 = tmax + pd.Timedelta.min - pd.Timedelta('1us')
    with pytest.raises(OverflowError, match=msg):
        tmax - t2