def test_to_csv_stringio(self, float_frame):
    buf = StringIO()
    float_frame.to_csv(buf)
    buf.seek(0)
    recons = read_csv(buf, index_col=0)
    tm.assert_frame_equal(recons, float_frame, check_names=False)