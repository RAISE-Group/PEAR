def test_dtypes(self):
    self._create_data()
    for f_name, d_name in product(self.funcs.keys(), self.data.keys()):
        f = self.funcs[f_name]
        d = self.data[d_name]
        exp = self.expects[d_name][f_name]
        self.check_dtypes(f, f_name, d, d_name, exp)