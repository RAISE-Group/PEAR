@pytest.mark.slow
def test_style_by_column(self):
    import matplotlib.pyplot as plt
    fig = plt.gcf()
    df = DataFrame(randn(100, 3))
    for markers in [{0: '^', 1: '+', 2: 'o'}, {0: '^', 1: '+'}, ['^', '+', 'o'], ['^', '+']]:
        fig.clf()
        fig.add_subplot(111)
        ax = df.plot(style=markers)
        for i, l in enumerate(ax.get_lines()[:len(markers)]):
            assert l.get_marker() == markers[i]