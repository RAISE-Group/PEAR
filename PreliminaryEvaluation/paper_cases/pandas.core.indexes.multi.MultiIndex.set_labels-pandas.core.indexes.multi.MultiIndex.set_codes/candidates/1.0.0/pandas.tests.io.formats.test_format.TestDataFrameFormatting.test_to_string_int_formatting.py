def test_to_string_int_formatting(self):
    df = DataFrame({'x': [-15, 20, 25, -35]})
    assert issubclass(df['x'].dtype.type, np.integer)
    output = df.to_string()
    expected = '    x\n0 -15\n1  20\n2  25\n3 -35'
    assert output == expected