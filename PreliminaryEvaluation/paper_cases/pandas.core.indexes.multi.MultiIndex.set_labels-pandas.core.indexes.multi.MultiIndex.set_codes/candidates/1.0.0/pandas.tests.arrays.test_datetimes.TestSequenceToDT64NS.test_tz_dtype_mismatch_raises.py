def test_tz_dtype_mismatch_raises(self):
    arr = DatetimeArray._from_sequence(['2000'], tz='US/Central')
    with pytest.raises(TypeError, match='data is already tz-aware'):
        sequence_to_dt64ns(arr, dtype=DatetimeTZDtype(tz='UTC'))