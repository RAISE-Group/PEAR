def test_numpy_transpose(self):
    msg = "the 'axes' parameter is not supported"
    s = tm.makeFloatSeries()
    tm.assert_series_equal(np.transpose(s), s)
    with pytest.raises(ValueError, match=msg):
        np.transpose(s, axes=1)
    df = tm.makeTimeDataFrame()
    tm.assert_frame_equal(np.transpose(np.transpose(df)), df)
    with pytest.raises(ValueError, match=msg):
        np.transpose(df, axes=1)