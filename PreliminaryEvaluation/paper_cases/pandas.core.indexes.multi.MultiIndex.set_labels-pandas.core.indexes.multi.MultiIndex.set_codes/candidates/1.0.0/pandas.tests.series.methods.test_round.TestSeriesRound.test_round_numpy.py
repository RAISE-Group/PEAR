def test_round_numpy(self):
    ser = Series([1.53, 1.36, 0.06])
    out = np.round(ser, decimals=0)
    expected = Series([2.0, 1.0, 0.0])
    tm.assert_series_equal(out, expected)
    msg = "the 'out' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.round(ser, decimals=0, out=ser)