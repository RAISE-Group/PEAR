@pytest.mark.slow
def test_if_scatterplot_colorbar_affects_xaxis_visibility(self):
    random_array = np.random.random((1000, 3))
    df = pd.DataFrame(random_array, columns=['A label', 'B label', 'C label'])
    ax1 = df.plot.scatter(x='A label', y='B label')
    ax2 = df.plot.scatter(x='A label', y='B label', c='C label')
    vis1 = [vis.get_visible() for vis in ax1.xaxis.get_minorticklabels()]
    vis2 = [vis.get_visible() for vis in ax2.xaxis.get_minorticklabels()]
    assert vis1 == vis2
    vis1 = [vis.get_visible() for vis in ax1.xaxis.get_majorticklabels()]
    vis2 = [vis.get_visible() for vis in ax2.xaxis.get_majorticklabels()]
    assert vis1 == vis2
    assert ax1.xaxis.get_label().get_visible() == ax2.xaxis.get_label().get_visible()