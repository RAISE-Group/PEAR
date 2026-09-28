def test_assign_bad(self):
    df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(TypeError):
        df.assign(lambda x: x.A)
    with pytest.raises(AttributeError):
        df.assign(C=df.A, D=df.A + df.C)