@pytest.mark.parametrize('x, y', [('x', 'y'), ('y', 'x'), ('y', 'y')])
@pytest.mark.slow
def test_plot_scatter_with_categorical_data(self, x, y):
    df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': pd.Categorical(['a', 'b', 'a', 'c'])})
    _check_plot_works(df.plot.scatter, x=x, y=y)