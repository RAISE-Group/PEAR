def check_dtypes(self, f, f_name, d, d_name, exp):
    roll = d.rolling(window=self.window)
    result = f(roll)
    tm.assert_almost_equal(result, exp)