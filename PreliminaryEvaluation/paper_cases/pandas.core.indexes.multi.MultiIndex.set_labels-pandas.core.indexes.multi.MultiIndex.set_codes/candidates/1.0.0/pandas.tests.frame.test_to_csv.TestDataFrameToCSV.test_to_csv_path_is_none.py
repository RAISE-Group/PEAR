def test_to_csv_path_is_none(self, float_frame):
    csv_str = float_frame.to_csv(path_or_buf=None)
    assert isinstance(csv_str, str)
    recons = pd.read_csv(StringIO(csv_str), index_col=0)
    tm.assert_frame_equal(float_frame, recons)