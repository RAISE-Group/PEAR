def test_plot_no_numeric_data(self):
    df = pd.Series(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        df.plot()