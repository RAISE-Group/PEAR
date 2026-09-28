def test_to_records_with_multindex(self):
    index = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
    data = np.zeros((8, 4))
    df = DataFrame(data, index=index)
    r = df.to_records(index=True)['level_0']
    assert 'bar' in r
    assert 'one' not in r