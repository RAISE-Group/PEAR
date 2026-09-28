def test_info_memory_usage_bug_on_multiindex(self):
    from string import ascii_uppercase as uppercase

    def memory_usage(f):
        return f.memory_usage(deep=True).sum()
    N = 100
    M = len(uppercase)
    index = pd.MultiIndex.from_product([list(uppercase), pd.date_range('20160101', periods=N)], names=['id', 'date'])
    df = DataFrame({'value': np.random.randn(N * M)}, index=index)
    unstacked = df.unstack('id')
    assert df.values.nbytes == unstacked.values.nbytes
    assert memory_usage(df) > memory_usage(unstacked)
    assert memory_usage(unstacked) - memory_usage(df) < 2000