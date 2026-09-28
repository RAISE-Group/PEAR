def test_query_empty_string(self):
    df = pd.DataFrame({'A': [1, 2, 3]})
    msg = 'expr cannot be an empty string'
    with pytest.raises(ValueError, match=msg):
        df.query('')