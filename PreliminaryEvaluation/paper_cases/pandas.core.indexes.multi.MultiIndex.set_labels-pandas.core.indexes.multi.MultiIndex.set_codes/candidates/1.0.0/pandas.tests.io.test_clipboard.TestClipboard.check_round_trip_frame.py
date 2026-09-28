def check_round_trip_frame(self, data, excel=None, sep=None, encoding=None):
    data.to_clipboard(excel=excel, sep=sep, encoding=encoding)
    result = read_clipboard(sep=sep or '\t', index_col=0, encoding=encoding)
    tm.assert_frame_equal(data, result, check_dtype=False)