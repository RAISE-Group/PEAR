def test_round_trip_frame_string(self, df):
    df.to_clipboard(excel=False, sep=None)
    result = read_clipboard()
    assert df.to_string() == result.to_string()
    assert df.shape == result.shape