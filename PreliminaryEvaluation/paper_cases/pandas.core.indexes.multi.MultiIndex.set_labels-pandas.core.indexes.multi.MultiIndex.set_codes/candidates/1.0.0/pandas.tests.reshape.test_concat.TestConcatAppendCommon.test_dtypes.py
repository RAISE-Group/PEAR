def test_dtypes(self):
    for typ, vals in self.data.items():
        self._check_expected_dtype(pd.Index(vals), typ)
        self._check_expected_dtype(pd.Series(vals), typ)