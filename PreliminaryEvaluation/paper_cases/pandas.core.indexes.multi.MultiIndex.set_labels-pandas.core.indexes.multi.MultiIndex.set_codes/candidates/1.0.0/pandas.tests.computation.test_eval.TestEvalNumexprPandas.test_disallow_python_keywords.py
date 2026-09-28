def test_disallow_python_keywords(self):
    df = pd.DataFrame([[0, 0, 0]], columns=['foo', 'bar', 'class'])
    msg = 'Python keyword not valid identifier in numexpr query'
    with pytest.raises(SyntaxError, match=msg):
        df.query('class == 0')
    df = pd.DataFrame()
    df.index.name = 'lambda'
    with pytest.raises(SyntaxError, match=msg):
        df.query('lambda == 0')