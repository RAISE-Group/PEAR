def test_identical(self):
    x = 1
    result = pd.eval('x', engine=self.engine, parser=self.parser)
    assert result == 1
    assert is_scalar(result)
    x = 1.5
    result = pd.eval('x', engine=self.engine, parser=self.parser)
    assert result == 1.5
    assert is_scalar(result)
    x = False
    result = pd.eval('x', engine=self.engine, parser=self.parser)
    assert not result
    assert is_bool(result)
    assert is_scalar(result)
    x = np.array([1])
    result = pd.eval('x', engine=self.engine, parser=self.parser)
    tm.assert_numpy_array_equal(result, np.array([1]))
    assert result.shape == (1,)
    x = np.array([1.5])
    result = pd.eval('x', engine=self.engine, parser=self.parser)
    tm.assert_numpy_array_equal(result, np.array([1.5]))
    assert result.shape == (1,)
    x = np.array([False])
    result = pd.eval('x', engine=self.engine, parser=self.parser)
    tm.assert_numpy_array_equal(result, np.array([False]))
    assert result.shape == (1,)