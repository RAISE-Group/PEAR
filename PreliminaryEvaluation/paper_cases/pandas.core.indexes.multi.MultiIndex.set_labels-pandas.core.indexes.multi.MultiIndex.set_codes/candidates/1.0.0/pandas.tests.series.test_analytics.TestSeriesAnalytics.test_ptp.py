def test_ptp(self):
    N = 1000
    arr = np.random.randn(N)
    ser = Series(arr)
    assert np.ptp(ser) == np.ptp(arr)