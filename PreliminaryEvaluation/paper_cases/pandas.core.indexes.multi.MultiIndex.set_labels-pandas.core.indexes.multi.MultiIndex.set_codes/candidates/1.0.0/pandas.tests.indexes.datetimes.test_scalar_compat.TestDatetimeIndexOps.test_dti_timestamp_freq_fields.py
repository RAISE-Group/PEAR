def test_dti_timestamp_freq_fields(self):
    idx = tm.makeDateIndex(100)
    assert idx.freq == Timestamp(idx[-1], idx.freq).freq
    assert idx.freqstr == Timestamp(idx[-1], idx.freq).freqstr