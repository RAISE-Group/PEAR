def test_replace_with_single_list(self):
    ser = pd.Series([0, 1, 2, 3, 4])
    result = ser.replace([1, 2, 3])
    tm.assert_series_equal(result, pd.Series([0, 0, 0, 0, 4]))
    s = ser.copy()
    s.replace([1, 2, 3], inplace=True)
    tm.assert_series_equal(s, pd.Series([0, 0, 0, 0, 4]))
    s = ser.copy()
    msg = 'Invalid fill method\\. Expecting pad \\(ffill\\) or backfill \\(bfill\\)\\. Got crash_cymbal'
    with pytest.raises(ValueError, match=msg):
        s.replace([1, 2, 3], inplace=True, method='crash_cymbal')
    tm.assert_series_equal(s, ser)