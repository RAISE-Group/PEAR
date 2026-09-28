@pytest.mark.slow
def test_bar_barwidth_position_int(self):
    df = DataFrame(randn(5, 5))
    for w in [1, 1.0]:
        ax = df.plot.bar(stacked=True, width=w)
        ticks = ax.xaxis.get_ticklocs()
        tm.assert_numpy_array_equal(ticks, np.array([0, 1, 2, 3, 4]))
        assert ax.get_xlim() == (-0.75, 4.75)
        assert ax.patches[0].get_x() == -0.5
        assert ax.patches[-1].get_x() == 3.5
    self._check_bar_alignment(df, kind='bar', stacked=True, width=1)
    self._check_bar_alignment(df, kind='barh', stacked=False, width=1)
    self._check_bar_alignment(df, kind='barh', stacked=True, width=1)
    self._check_bar_alignment(df, kind='bar', subplots=True, width=1)
    self._check_bar_alignment(df, kind='barh', subplots=True, width=1)