def test_contiguous_boolean_preserve_freq(self):
    rng = date_range('1/1/2000', '3/1/2000', freq='B')
    mask = np.zeros(len(rng), dtype=bool)
    mask[10:20] = True
    masked = rng[mask]
    expected = rng[10:20]
    assert expected.freq is not None
    assert_range_equal(masked, expected)
    mask[22] = True
    masked = rng[mask]
    assert masked.freq is None