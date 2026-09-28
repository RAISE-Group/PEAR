def test_frame_datetime64_pre1900_repr(self):
    df = DataFrame({'year': date_range('1/1/1700', periods=50, freq='A-DEC')})
    repr(df)