def test_align_series_frame(self, data, na_value):
    ser = pd.Series(data, name='a')
    df = pd.DataFrame({'col': np.arange(len(ser) + 1)})
    r1, r2 = ser.align(df)
    e1 = pd.Series(data._from_sequence(list(data) + [na_value], dtype=data.dtype), name=ser.name)
    self.assert_series_equal(r1, e1)
    self.assert_frame_equal(r2, df)