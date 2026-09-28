@pytest.mark.slow
def test_plot_int_columns(self):
    df = DataFrame(randn(100, 4)).cumsum()
    _check_plot_works(df.plot, legend=True)