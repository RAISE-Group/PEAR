def test_mixed_comparison(self):
    df = pd.DataFrame([['1989-08-01', 1], ['1989-08-01', 2]])
    other = pd.DataFrame([['a', 'b'], ['c', 'd']])
    result = df == other
    assert not result.any().any()
    result = df != other
    assert result.all().all()