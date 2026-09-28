def test_reset_index_right_dtype(self):
    time = np.arange(0.0, 10, np.sqrt(2) / 2)
    s1 = Series(9.81 * time ** 2 / 2, index=Index(time, name='time'), name='speed')
    df = DataFrame(s1)
    resetted = s1.reset_index()
    assert resetted['time'].dtype == np.float64
    resetted = df.reset_index()
    assert resetted['time'].dtype == np.float64