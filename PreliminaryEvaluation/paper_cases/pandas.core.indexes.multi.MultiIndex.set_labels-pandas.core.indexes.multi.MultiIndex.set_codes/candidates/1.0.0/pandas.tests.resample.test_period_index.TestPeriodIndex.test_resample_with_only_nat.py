def test_resample_with_only_nat(self):
    pi = PeriodIndex([pd.NaT] * 3, freq='S')
    frame = DataFrame([2, 3, 5], index=pi)
    expected_index = PeriodIndex(data=[], freq=pi.freq)
    expected = DataFrame(index=expected_index)
    result = frame.resample('1s').mean()
    tm.assert_frame_equal(result, expected)