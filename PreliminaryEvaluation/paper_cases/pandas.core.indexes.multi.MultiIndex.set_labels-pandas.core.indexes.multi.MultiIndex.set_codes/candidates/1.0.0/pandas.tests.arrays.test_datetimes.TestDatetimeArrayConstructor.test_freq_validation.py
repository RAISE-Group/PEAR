def test_freq_validation(self):
    arr = np.arange(5, dtype=np.int64) * 3600 * 10 ** 9
    msg = 'Inferred frequency H from passed values does not conform to passed frequency W-SUN'
    with pytest.raises(ValueError, match=msg):
        DatetimeArray(arr, freq='W')