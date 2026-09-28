def test_constructor_multi_index(self):
    tuples = [(2, 3), (3, 3), (3, 3)]
    mi = MultiIndex.from_tuples(tuples)
    df = DataFrame(index=mi, columns=mi)
    assert pd.isna(df).values.ravel().all()
    tuples = [(3, 3), (2, 3), (3, 3)]
    mi = MultiIndex.from_tuples(tuples)
    df = DataFrame(index=mi, columns=mi)
    assert pd.isna(df).values.ravel().all()