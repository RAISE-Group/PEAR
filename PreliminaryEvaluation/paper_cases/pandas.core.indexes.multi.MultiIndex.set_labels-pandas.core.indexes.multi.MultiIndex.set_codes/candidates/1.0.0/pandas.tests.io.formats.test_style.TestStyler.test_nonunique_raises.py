def test_nonunique_raises(self):
    df = pd.DataFrame([[1, 2]], columns=['A', 'A'])
    with pytest.raises(ValueError):
        df.style
    with pytest.raises(ValueError):
        Styler(df)