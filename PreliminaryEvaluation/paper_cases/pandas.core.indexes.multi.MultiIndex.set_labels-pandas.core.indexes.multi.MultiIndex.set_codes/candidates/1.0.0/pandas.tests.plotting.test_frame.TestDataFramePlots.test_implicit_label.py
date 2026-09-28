@pytest.mark.slow
def test_implicit_label(self):
    df = DataFrame(randn(10, 3), columns=['a', 'b', 'c'])
    ax = df.plot(x='a', y='b')
    self._check_text_labels(ax.xaxis.get_label(), 'a')