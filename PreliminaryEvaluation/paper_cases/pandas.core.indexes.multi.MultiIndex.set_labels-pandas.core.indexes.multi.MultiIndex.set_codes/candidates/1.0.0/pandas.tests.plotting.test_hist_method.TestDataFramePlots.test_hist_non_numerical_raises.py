@pytest.mark.slow
def test_hist_non_numerical_raises(self):
    df = DataFrame(np.random.rand(10, 2))
    df_o = df.astype(np.object)
    msg = 'hist method requires numerical columns, nothing to plot.'
    with pytest.raises(ValueError, match=msg):
        df_o.hist()