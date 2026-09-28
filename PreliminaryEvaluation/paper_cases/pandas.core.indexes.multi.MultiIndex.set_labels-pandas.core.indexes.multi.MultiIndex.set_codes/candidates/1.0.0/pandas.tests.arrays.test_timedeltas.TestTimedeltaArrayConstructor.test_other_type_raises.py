def test_other_type_raises(self):
    with pytest.raises(ValueError, match='dtype bool cannot be converted'):
        TimedeltaArray(np.array([1, 2, 3], dtype='bool'))