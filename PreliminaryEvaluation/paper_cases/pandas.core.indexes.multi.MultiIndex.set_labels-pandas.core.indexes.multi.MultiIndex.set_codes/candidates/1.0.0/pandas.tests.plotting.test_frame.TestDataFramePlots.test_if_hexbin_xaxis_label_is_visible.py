@pytest.mark.slow
def test_if_hexbin_xaxis_label_is_visible(self):
    random_array = np.random.random((1000, 3))
    df = pd.DataFrame(random_array, columns=['A label', 'B label', 'C label'])
    ax = df.plot.hexbin('A label', 'B label', gridsize=12)
    assert all((vis.get_visible() for vis in ax.xaxis.get_minorticklabels()))
    assert all((vis.get_visible() for vis in ax.xaxis.get_majorticklabels()))
    assert ax.xaxis.get_label().get_visible()