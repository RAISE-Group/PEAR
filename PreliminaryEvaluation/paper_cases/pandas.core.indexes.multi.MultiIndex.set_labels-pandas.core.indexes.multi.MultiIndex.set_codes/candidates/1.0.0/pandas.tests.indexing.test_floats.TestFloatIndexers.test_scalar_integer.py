def test_scalar_integer(self):
    for i in [Int64Index(range(5)), RangeIndex(5)]:
        for s in [Series(np.arange(len(i))), DataFrame(np.random.randn(len(i), len(i)), index=i, columns=i)]:
            for idxr, getitem in [(lambda x: x.loc, False), (lambda x: x, True)]:
                result = idxr(s)[3.0]
                self.check(result, s, 3, getitem)
            for idxr, getitem in [(lambda x: x.loc, False), (lambda x: x, True)]:
                if isinstance(s, Series):

                    def compare(x, y):
                        assert x == y
                    expected = 100
                else:
                    compare = tm.assert_series_equal
                    if getitem:
                        expected = Series(100, index=range(len(s)), name=3)
                    else:
                        expected = Series(100.0, index=range(len(s)), name=3)
                s2 = s.copy()
                idxr(s2)[3.0] = 100
                result = idxr(s2)[3.0]
                compare(result, expected)
                result = idxr(s2)[3]
                compare(result, expected)
            assert 3.0 in s