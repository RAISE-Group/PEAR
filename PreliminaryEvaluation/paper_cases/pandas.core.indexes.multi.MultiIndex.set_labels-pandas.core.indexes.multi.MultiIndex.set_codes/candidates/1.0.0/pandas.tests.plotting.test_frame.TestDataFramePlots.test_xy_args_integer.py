@pytest.mark.parametrize('x,y,colnames', [(0, 1, ['A', 'B']), (1, 0, [0, 1])])
def test_xy_args_integer(self, x, y, colnames):
    df = DataFrame({'A': [1, 2], 'B': [3, 4]})
    df.columns = colnames
    _check_plot_works(df.plot, x=x, y=y)