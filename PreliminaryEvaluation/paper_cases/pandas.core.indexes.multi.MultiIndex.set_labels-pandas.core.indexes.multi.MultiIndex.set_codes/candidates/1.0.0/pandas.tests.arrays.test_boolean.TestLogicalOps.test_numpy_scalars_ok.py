def test_numpy_scalars_ok(self, all_logical_operators):
    a = pd.array([True, False, None], dtype='boolean')
    op = getattr(a, all_logical_operators)
    tm.assert_extension_array_equal(op(True), op(np.bool(True)))
    tm.assert_extension_array_equal(op(False), op(np.bool(False)))