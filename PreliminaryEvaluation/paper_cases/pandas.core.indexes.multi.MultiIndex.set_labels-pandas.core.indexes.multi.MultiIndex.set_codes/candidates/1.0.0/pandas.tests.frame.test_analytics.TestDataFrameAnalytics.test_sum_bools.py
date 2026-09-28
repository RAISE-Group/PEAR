def test_sum_bools(self):
    df = DataFrame(index=range(1), columns=range(10))
    bools = isna(df)
    assert bools.sum(axis=1)[0] == 10