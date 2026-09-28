@pytest.mark.slow
def test_hist_bins_legacy(self):
    df = DataFrame(np.random.randn(10, 2))
    ax = df.hist(bins=2)[0][0]
    assert len(ax.patches) == 2