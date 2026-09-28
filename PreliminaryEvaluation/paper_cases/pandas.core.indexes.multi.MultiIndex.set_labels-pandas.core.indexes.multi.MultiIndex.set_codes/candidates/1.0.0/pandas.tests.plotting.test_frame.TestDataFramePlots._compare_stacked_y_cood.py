def _compare_stacked_y_cood(self, normal_lines, stacked_lines):
    base = np.zeros(len(normal_lines[0].get_data()[1]))
    for nl, sl in zip(normal_lines, stacked_lines):
        base += nl.get_data()[1]
        sy = sl.get_data()[1]
        tm.assert_numpy_array_equal(base, sy)