def test_sample_is_copy(self):
    df = pd.DataFrame(np.random.randn(10, 3), columns=['a', 'b', 'c'])
    df2 = df.sample(3)
    with tm.assert_produces_warning(None):
        df2['d'] = 1