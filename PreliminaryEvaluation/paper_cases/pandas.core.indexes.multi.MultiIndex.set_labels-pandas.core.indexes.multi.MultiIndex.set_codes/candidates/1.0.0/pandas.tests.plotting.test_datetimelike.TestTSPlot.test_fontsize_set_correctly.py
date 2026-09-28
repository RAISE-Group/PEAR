def test_fontsize_set_correctly(self):
    df = DataFrame(np.random.randn(10, 9), index=range(10))
    fig, ax = self.plt.subplots()
    df.plot(fontsize=2, ax=ax)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        assert label.get_fontsize() == 2