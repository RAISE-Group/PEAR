def test_accessor_raises(self):
    df = pd.DataFrame({'A': [0, 1]})
    with pytest.raises(AttributeError, match='sparse'):
        df.sparse