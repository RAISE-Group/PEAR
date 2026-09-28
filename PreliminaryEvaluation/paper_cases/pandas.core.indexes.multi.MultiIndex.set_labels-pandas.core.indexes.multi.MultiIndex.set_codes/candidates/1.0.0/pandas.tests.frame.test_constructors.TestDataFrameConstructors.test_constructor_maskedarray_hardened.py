def test_constructor_maskedarray_hardened(self):
    mat_hard = ma.masked_all((2, 2), dtype=float).harden_mask()
    result = pd.DataFrame(mat_hard, columns=['A', 'B'], index=[1, 2])
    expected = pd.DataFrame({'A': [np.nan, np.nan], 'B': [np.nan, np.nan]}, columns=['A', 'B'], index=[1, 2], dtype=float)
    tm.assert_frame_equal(result, expected)
    mat_hard = ma.ones((2, 2), dtype=float).harden_mask()
    result = pd.DataFrame(mat_hard, columns=['A', 'B'], index=[1, 2])
    expected = pd.DataFrame({'A': [1.0, 1.0], 'B': [1.0, 1.0]}, columns=['A', 'B'], index=[1, 2], dtype=float)
    tm.assert_frame_equal(result, expected)