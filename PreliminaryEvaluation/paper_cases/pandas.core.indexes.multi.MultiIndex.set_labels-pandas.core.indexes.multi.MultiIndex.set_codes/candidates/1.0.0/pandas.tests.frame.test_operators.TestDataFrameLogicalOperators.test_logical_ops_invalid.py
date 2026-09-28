def test_logical_ops_invalid(self):
    df1 = DataFrame(1.0, index=[1], columns=['A'])
    df2 = DataFrame(True, index=[1], columns=['A'])
    with pytest.raises(TypeError):
        df1 | df2
    df1 = DataFrame('foo', index=[1], columns=['A'])
    df2 = DataFrame(True, index=[1], columns=['A'])
    with pytest.raises(TypeError):
        df1 | df2