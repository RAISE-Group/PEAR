def test_error(self):
    for obj in [pd.Series([1, 2, 3]), 1, 'foo', pd.Timestamp('20130101'), np.array([1, 2, 3])]:
        self.check_error_on_write(obj, ValueError)