def test_iter_python_types(self):
    cat = Categorical([1, 2])
    assert isinstance(list(cat)[0], int)
    assert isinstance(cat.tolist()[0], int)