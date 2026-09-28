def check_dtypes(self, f, f_name, d, d_name, exp):
    roll = d.rolling(window=self.window)
    if f_name == 'count':
        result = f(roll)
        tm.assert_almost_equal(result, exp)
    else:
        with pytest.raises(DataError):
            f(roll)