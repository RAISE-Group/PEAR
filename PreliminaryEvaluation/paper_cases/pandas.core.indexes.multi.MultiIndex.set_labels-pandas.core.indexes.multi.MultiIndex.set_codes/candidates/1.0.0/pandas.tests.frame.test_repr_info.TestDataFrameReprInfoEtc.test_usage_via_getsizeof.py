@pytest.mark.skipif(PYPY, reason='PyPy getsizeof() fails by design')
def test_usage_via_getsizeof(self):
    df = DataFrame(data=1, index=pd.MultiIndex.from_product([['a'], range(1000)]), columns=['A'])
    mem = df.memory_usage(deep=True).sum()
    diff = mem - sys.getsizeof(df)
    assert abs(diff) < 100