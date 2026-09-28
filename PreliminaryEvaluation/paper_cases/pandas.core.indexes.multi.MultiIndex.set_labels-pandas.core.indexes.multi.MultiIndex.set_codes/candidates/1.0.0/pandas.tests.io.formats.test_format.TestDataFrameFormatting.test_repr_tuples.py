def test_repr_tuples(self):
    buf = StringIO()
    df = DataFrame({'tups': list(zip(range(10), range(10)))})
    repr(df)
    df.to_string(col_space=10, buf=buf)