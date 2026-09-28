@pytest.mark.slow
def test_hist_no_overlap(self):
    from matplotlib.pyplot import subplot, gcf
    x = Series(randn(2))
    y = Series(randn(2))
    subplot(121)
    x.hist()
    subplot(122)
    y.hist()
    fig = gcf()
    axes = fig.axes
    assert len(axes) == 2