@pytest.mark.slow
def test_secondary_y_mixed_freq_ts_xlim(self):
    rng = date_range('2000-01-01', periods=10000, freq='min')
    ts = Series(1, index=rng)
    _, ax = self.plt.subplots()
    ts.plot(ax=ax)
    left_before, right_before = ax.get_xlim()
    ts.resample('D').mean().plot(secondary_y=True, ax=ax)
    left_after, right_after = ax.get_xlim()
    assert left_before == left_after
    assert right_before == right_after