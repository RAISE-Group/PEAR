def test_categorical(self):
    c = Categorical([1, 2])
    exp = c
    tm.assert_categorical_equal(algos.mode(c), exp)
    tm.assert_categorical_equal(c.mode(), exp)
    c = Categorical([1, 'a', 'a'])
    exp = Categorical(['a'], categories=[1, 'a'])
    tm.assert_categorical_equal(algos.mode(c), exp)
    tm.assert_categorical_equal(c.mode(), exp)
    c = Categorical([1, 1, 2, 3, 3])
    exp = Categorical([1, 3], categories=[1, 2, 3])
    tm.assert_categorical_equal(algos.mode(c), exp)
    tm.assert_categorical_equal(c.mode(), exp)