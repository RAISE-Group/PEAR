@pytest.mark.parametrize('x,y', [('A', 'B'), (['A'], 'B')])
def test_invalid_xy_args_dup_cols(self, x, y):
    df = DataFrame([[1, 3, 5], [2, 4, 6]], columns=list('AAB'))
    with pytest.raises(ValueError):
        df.plot(x=x, y=y)