def test_put_integer(self, setup_path):
    df = DataFrame(np.random.randn(50, 100))
    self._check_roundtrip(df, tm.assert_frame_equal, setup_path)