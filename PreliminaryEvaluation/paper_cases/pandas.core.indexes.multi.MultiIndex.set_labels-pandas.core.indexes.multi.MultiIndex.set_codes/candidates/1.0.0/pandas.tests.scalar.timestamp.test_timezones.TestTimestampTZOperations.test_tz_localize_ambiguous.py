def test_tz_localize_ambiguous(self):
    ts = Timestamp('2014-11-02 01:00')
    ts_dst = ts.tz_localize('US/Eastern', ambiguous=True)
    ts_no_dst = ts.tz_localize('US/Eastern', ambiguous=False)
    assert (ts_no_dst.value - ts_dst.value) / 1000000000.0 == 3600
    with pytest.raises(ValueError):
        ts.tz_localize('US/Eastern', ambiguous='infer')
    msg = 'Cannot localize tz-aware Timestamp, use tz_convert for conversions'
    with pytest.raises(TypeError, match=msg):
        Timestamp('2011-01-01', tz='US/Eastern').tz_localize('Asia/Tokyo')
    msg = 'Cannot convert tz-naive Timestamp, use tz_localize to localize'
    with pytest.raises(TypeError, match=msg):
        Timestamp('2011-01-01').tz_convert('Asia/Tokyo')