def test_conv_read_write(self, setup_path):
    path = create_tempfile(setup_path)
    try:

        def roundtrip(key, obj, **kwargs):
            obj.to_hdf(path, key, **kwargs)
            return read_hdf(path, key)
        o = tm.makeTimeSeries()
        tm.assert_series_equal(o, roundtrip('series', o))
        o = tm.makeStringSeries()
        tm.assert_series_equal(o, roundtrip('string_series', o))
        o = tm.makeDataFrame()
        tm.assert_frame_equal(o, roundtrip('frame', o))
        df = DataFrame(dict(A=range(5), B=range(5)))
        df.to_hdf(path, 'table', append=True)
        result = read_hdf(path, 'table', where=['index>2'])
        tm.assert_frame_equal(df[df.index > 2], result)
    finally:
        safe_remove(path)