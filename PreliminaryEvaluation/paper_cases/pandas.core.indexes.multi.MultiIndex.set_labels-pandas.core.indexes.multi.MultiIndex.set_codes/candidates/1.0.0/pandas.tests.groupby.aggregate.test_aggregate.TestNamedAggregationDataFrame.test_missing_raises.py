def test_missing_raises(self):
    df = pd.DataFrame({'A': [0, 1], 'B': [1, 2]})
    with pytest.raises(KeyError, match="Column 'C' does not exist"):
        df.groupby('A').agg(c=('C', 'sum'))