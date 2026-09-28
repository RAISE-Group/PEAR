def test_stringify_columns(self):
    df = pd.DataFrame(np.arange(12).reshape(4, 3)).copy()
    self.check_error_on_write(df, ValueError)