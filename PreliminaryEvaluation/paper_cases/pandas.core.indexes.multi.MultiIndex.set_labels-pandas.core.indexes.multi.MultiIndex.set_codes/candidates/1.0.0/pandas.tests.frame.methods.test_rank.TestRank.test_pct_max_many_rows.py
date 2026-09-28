@pytest.mark.single
@pytest.mark.high_memory
def test_pct_max_many_rows(self):
    df = DataFrame({'A': np.arange(2 ** 24 + 1), 'B': np.arange(2 ** 24 + 1, 0, -1)})
    result = df.rank(pct=True).max()
    assert (result == 1).all()