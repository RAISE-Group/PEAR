def test_line_use_index_false(self):
    s = Series([1, 2, 3], index=['a', 'b', 'c'])
    s.index.name = 'The Index'
    _, ax = self.plt.subplots()
    ax = s.plot(use_index=False, ax=ax)
    label = ax.get_xlabel()
    assert label == ''
    _, ax = self.plt.subplots()
    ax2 = s.plot.bar(use_index=False, ax=ax)
    label2 = ax2.get_xlabel()
    assert label2 == ''