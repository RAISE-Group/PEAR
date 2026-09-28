def test_freq_validation(self):
    arr = np.array([0, 0, 1], dtype=np.int64) * 3600 * 10 ** 9
    msg = 'Inferred frequency None from passed values does not conform to passed frequency D'
    with pytest.raises(ValueError, match=msg):
        TimedeltaArray(arr.view('timedelta64[ns]'), freq='D')