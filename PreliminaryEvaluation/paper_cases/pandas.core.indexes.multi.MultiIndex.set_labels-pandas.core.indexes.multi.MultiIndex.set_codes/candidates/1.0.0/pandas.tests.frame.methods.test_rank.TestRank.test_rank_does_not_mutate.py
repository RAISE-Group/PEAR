def test_rank_does_not_mutate(self):
    df = DataFrame(np.random.randn(10, 3), dtype='float64')
    expected = df.copy()
    df.rank()
    result = df
    tm.assert_frame_equal(result, expected)