def test_nanstd_roundoff(self):
    data = Series(766897346 * np.ones(10))
    for ddof in range(3):
        result = data.std(ddof=ddof)
        assert result == 0.0