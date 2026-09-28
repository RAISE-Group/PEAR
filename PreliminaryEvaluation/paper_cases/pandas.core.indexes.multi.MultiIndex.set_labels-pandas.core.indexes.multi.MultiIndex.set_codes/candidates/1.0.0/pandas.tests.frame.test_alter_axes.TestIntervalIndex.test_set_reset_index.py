def test_set_reset_index(self):
    df = DataFrame({'A': range(10)})
    s = cut(df.A, 5)
    df['B'] = s
    df = df.set_index('B')
    df = df.reset_index()