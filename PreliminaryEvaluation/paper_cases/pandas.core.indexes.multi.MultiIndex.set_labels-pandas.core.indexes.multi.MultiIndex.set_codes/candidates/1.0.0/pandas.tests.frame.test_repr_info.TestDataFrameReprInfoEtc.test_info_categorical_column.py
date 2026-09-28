def test_info_categorical_column(self):
    n = 2500
    df = DataFrame({'int64': np.random.randint(100, size=n)})
    df['category'] = Series(np.array(list('abcdefghij')).take(np.random.randint(0, 10, size=n))).astype('category')
    df.isna()
    buf = StringIO()
    df.info(buf=buf)
    df2 = df[df['category'] == 'd']
    buf = StringIO()
    df2.info(buf=buf)