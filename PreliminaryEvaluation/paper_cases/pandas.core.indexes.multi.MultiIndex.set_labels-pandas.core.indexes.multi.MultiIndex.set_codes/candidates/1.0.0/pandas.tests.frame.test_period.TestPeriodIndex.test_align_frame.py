def test_align_frame(self):
    rng = period_range('1/1/2000', '1/1/2010', freq='A')
    ts = DataFrame(np.random.randn(len(rng), 3), index=rng)
    result = ts + ts[::2]
    expected = ts + ts
    expected.values[1::2] = np.nan
    tm.assert_frame_equal(result, expected)
    result = ts + _permute(ts[::2])
    tm.assert_frame_equal(result, expected)