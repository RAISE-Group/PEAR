def test_insert_benchmark(self):
    N = 10
    K = 5
    df = DataFrame(index=range(N))
    new_col = np.random.randn(N)
    for i in range(K):
        df[i] = new_col
    expected = DataFrame(np.repeat(new_col, K).reshape(N, K), index=range(N))
    tm.assert_frame_equal(df, expected)