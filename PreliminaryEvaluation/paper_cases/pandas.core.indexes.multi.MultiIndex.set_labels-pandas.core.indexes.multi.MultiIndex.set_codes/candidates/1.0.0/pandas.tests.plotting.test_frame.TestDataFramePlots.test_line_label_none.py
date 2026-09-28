@pytest.mark.slow
def test_line_label_none(self):
    s = Series([1, 2])
    ax = s.plot()
    assert ax.get_legend() is None
    ax = s.plot(legend=True)
    assert ax.get_legend().get_texts()[0].get_text() == 'None'