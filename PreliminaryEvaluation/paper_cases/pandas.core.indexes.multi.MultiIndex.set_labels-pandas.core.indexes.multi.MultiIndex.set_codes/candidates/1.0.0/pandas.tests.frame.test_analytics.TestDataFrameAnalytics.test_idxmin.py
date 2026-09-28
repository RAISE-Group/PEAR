def test_idxmin(self, float_frame, int_frame):
    frame = float_frame
    frame.loc[5:10] = np.nan
    frame.loc[15:20, -2:] = np.nan
    for skipna in [True, False]:
        for axis in [0, 1]:
            for df in [frame, int_frame]:
                result = df.idxmin(axis=axis, skipna=skipna)
                expected = df.apply(Series.idxmin, axis=axis, skipna=skipna)
                tm.assert_series_equal(result, expected)
    msg = "No axis named 2 for object type <class 'pandas.core.frame.DataFrame'>"
    with pytest.raises(ValueError, match=msg):
        frame.idxmin(axis=2)