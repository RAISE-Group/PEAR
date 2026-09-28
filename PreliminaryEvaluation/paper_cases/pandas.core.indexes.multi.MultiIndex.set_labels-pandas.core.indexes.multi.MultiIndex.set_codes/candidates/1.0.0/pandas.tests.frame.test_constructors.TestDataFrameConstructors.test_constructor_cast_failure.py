def test_constructor_cast_failure(self):
    foo = DataFrame({'a': ['a', 'b', 'c']}, dtype=np.float64)
    assert foo['a'].dtype == object
    df = DataFrame(np.ones((4, 2)))
    df['foo'] = np.ones((4, 2)).tolist()
    msg = 'Wrong number of items passed 2, placement implies 1'
    with pytest.raises(ValueError, match=msg):
        df['test'] = np.ones((4, 2))
    df['foo2'] = np.ones((4, 2)).tolist()