def test_iter_python_types_datetime(self):
    cat = Categorical([Timestamp('2017-01-01'), Timestamp('2017-01-02')])
    assert isinstance(list(cat)[0], Timestamp)
    assert isinstance(cat.tolist()[0], Timestamp)