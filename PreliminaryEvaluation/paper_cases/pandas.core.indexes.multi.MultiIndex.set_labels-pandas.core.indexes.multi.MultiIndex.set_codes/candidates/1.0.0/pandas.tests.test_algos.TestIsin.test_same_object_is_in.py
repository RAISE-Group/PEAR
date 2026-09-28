def test_same_object_is_in(self):

    class LikeNan:

        def __eq__(self, other) -> bool:
            return False

        def __hash__(self):
            return 0
    a, b = (LikeNan(), LikeNan())
    tm.assert_numpy_array_equal(algos.isin([a], [a]), np.array([True]))
    tm.assert_numpy_array_equal(algos.isin([a], [b]), np.array([False]))