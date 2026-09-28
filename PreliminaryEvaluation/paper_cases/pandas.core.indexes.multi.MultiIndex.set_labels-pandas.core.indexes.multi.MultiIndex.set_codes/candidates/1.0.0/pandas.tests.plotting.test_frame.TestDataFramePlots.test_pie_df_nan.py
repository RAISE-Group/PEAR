def test_pie_df_nan(self):
    df = DataFrame(np.random.rand(4, 4))
    for i in range(4):
        df.iloc[i, i] = np.nan
    fig, axes = self.plt.subplots(ncols=4)
    df.plot.pie(subplots=True, ax=axes, legend=True)
    base_expected = ['0', '1', '2', '3']
    for i, ax in enumerate(axes):
        expected = list(base_expected)
        expected[i] = ''
        result = [x.get_text() for x in ax.texts]
        assert result == expected
        assert [x.get_text() for x in ax.get_legend().get_texts()] == base_expected[:i] + base_expected[i + 1:]