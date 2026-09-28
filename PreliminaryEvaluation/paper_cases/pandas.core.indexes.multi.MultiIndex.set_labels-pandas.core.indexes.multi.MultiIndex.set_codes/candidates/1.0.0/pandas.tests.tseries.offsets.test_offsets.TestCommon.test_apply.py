def test_apply(self, offset_types):
    sdt = datetime(2011, 1, 1, 9, 0)
    ndt = np_datetime64_compat('2011-01-01 09:00Z')
    for dt in [sdt, ndt]:
        expected = self.expecteds[offset_types.__name__]
        self._check_offsetfunc_works(offset_types, 'apply', dt, expected)
        expected = Timestamp(expected.date())
        self._check_offsetfunc_works(offset_types, 'apply', dt, expected, normalize=True)