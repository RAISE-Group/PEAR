@pytest.mark.single
@pytest.mark.high_memory
@pytest.mark.parametrize('values', [np.arange(2 ** 24 + 1), np.arange(2 ** 25 + 2).reshape(2 ** 24 + 1, 2)], ids=['1d', '2d'])
def test_pct_max_many_rows(self, values):
    result = algos.rank(values, pct=True).max()
    assert result == 1