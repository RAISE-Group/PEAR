def test_plot_no_numeric_data(self):
    df = pd.DataFrame(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        df.plot()