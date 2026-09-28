def test_to_csv_from_csv_w_all_infs(self, float_frame):
    float_frame['E'] = np.inf
    float_frame['F'] = -np.inf
    with tm.ensure_clean() as path:
        float_frame.to_csv(path)
        recons = self.read_csv(path)
        tm.assert_frame_equal(float_frame, recons, check_names=False)
        tm.assert_frame_equal(np.isinf(float_frame), np.isinf(recons), check_names=False)