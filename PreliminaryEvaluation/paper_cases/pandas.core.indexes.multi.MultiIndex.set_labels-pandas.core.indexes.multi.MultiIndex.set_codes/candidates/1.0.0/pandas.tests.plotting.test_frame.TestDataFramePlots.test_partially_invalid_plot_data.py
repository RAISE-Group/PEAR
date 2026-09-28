@pytest.mark.slow
def test_partially_invalid_plot_data(self):
    with tm.RNGContext(42):
        df = DataFrame(randn(10, 2), dtype=object)
        df[np.random.rand(df.shape[0]) > 0.5] = 'a'
        for kind in plotting.PlotAccessor._common_kinds:
            msg = 'no numeric data to plot'
            with pytest.raises(TypeError, match=msg):
                df.plot(kind=kind)
    with tm.RNGContext(42):
        kinds = ['area']
        df = DataFrame(rand(10, 2), dtype=object)
        df[np.random.rand(df.shape[0]) > 0.5] = 'a'
        for kind in kinds:
            with pytest.raises(TypeError):
                df.plot(kind=kind)