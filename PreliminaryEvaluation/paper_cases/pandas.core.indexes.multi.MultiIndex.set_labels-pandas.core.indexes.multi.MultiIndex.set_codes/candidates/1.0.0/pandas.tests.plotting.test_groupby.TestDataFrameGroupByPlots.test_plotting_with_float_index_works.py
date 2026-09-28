def test_plotting_with_float_index_works(self):
    df = DataFrame({'def': [1, 1, 1, 2, 2, 2, 3, 3, 3], 'val': np.random.randn(9)}, index=[1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0])
    df.groupby('def')['val'].plot()
    tm.close()
    df.groupby('def')['val'].apply(lambda x: x.plot())
    tm.close()