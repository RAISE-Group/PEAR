def test_slice_float(self):
    index = Index(np.arange(5.0)) + 0.1
    for s in [Series(range(5), index=index), DataFrame(np.random.randn(5, 2), index=index)]:
        for l in [slice(3.0, 4), slice(3, 4.0), slice(3.0, 4.0)]:
            expected = s.iloc[3:4]
            for idxr in [lambda x: x.loc, lambda x: x]:
                result = idxr(s)[l]
                if isinstance(s, Series):
                    tm.assert_series_equal(result, expected)
                else:
                    tm.assert_frame_equal(result, expected)
                s2 = s.copy()
                idxr(s2)[l] = 0
                result = idxr(s2)[l].values.ravel()
                assert (result == 0).all()