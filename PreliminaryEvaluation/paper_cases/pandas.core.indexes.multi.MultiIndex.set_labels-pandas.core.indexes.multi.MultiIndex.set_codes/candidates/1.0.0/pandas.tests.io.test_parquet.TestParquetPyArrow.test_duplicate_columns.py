def test_duplicate_columns(self, pa):
    df = pd.DataFrame(np.arange(12).reshape(4, 3), columns=list('aaa')).copy()
    self.check_error_on_write(df, pa, ValueError)