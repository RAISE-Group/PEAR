def test_corr_sanity(self):
    df = DataFrame(np.array([[0.87024726, 0.18505595], [0.64355431, 0.3091617], [0.92372966, 0.50552513], [0.00203756, 0.04520709], [0.84780328, 0.33394331], [0.78369152, 0.63919667]]))
    res = df[0].rolling(5, center=True).corr(df[1])
    assert all((np.abs(np.nan_to_num(x)) <= 1 for x in res))
    for _ in range(10):
        df = DataFrame(np.random.rand(30, 2))
        res = df[0].rolling(5, center=True).corr(df[1])
        try:
            assert all((np.abs(np.nan_to_num(x)) <= 1 for x in res))
        except AssertionError:
            print(res)