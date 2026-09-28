def test_pad_require_monotonicity(self):
    rng = date_range('1/1/2000', '3/1/2000', freq='B')
    rng2 = rng[[1, 0, 2]]
    msg = 'index must be monotonic increasing or decreasing'
    with pytest.raises(ValueError, match=msg):
        rng2.get_indexer(rng, method='pad')