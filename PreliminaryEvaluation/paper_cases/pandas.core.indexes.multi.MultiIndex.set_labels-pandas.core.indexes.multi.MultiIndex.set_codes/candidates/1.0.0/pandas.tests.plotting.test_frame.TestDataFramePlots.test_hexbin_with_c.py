@pytest.mark.slow
def test_hexbin_with_c(self):
    df = self.hexbin_df
    ax = df.plot.hexbin(x='A', y='B', C='C')
    assert len(ax.collections) == 1
    ax = df.plot.hexbin(x='A', y='B', C='C', reduce_C_function=np.std)
    assert len(ax.collections) == 1