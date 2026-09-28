@pytest.mark.parametrize('args,kwargs', [((ChainMap({'A': 'a'}, {'B': 'b'}),), dict(axis='columns')), ((), dict(columns=ChainMap({'A': 'a'}, {'B': 'b'})))])
def test_rename_chainmap(self, args, kwargs):
    colAData = range(1, 11)
    colBdata = np.random.randn(10)
    df = DataFrame({'A': colAData, 'B': colBdata})
    result = df.rename(*args, **kwargs)
    expected = DataFrame({'a': colAData, 'b': colBdata})
    tm.assert_frame_equal(result, expected)