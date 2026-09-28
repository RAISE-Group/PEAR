def test_divmod(self):

    def check(series, other):
        results = divmod(series, other)
        if isinstance(other, abc.Iterable) and len(series) != len(other):
            other_np = []
            for n in other:
                other_np.append(n)
                other_np.append(np.nan)
        else:
            other_np = other
        other_np = np.asarray(other_np)
        with np.errstate(all='ignore'):
            expecteds = divmod(series.values, np.asarray(other_np))
        for result, expected in zip(results, expecteds):
            tm.assert_almost_equal(np.asarray(result), expected)
            assert result.name == series.name
            tm.assert_index_equal(result.index, series.index)
    tser = tm.makeTimeSeries().rename('ts')
    check(tser, tser * 2)
    check(tser, tser[::2])
    check(tser, 5)