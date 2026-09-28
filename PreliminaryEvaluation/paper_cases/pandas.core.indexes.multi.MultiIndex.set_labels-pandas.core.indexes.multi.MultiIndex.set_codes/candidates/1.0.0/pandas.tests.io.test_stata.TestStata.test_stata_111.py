def test_stata_111(self):
    df = read_stata(self.dta24_111)
    original = pd.DataFrame({'y': [1, 1, 1, 1, 1, 0, 0, np.NaN, 0, 0], 'x': [1, 2, 1, 3, np.NaN, 4, 3, 5, 1, 6], 'w': [2, np.NaN, 5, 2, 4, 4, 3, 1, 2, 3], 'z': ['a', 'b', 'c', 'd', 'e', '', 'g', 'h', 'i', 'j']})
    original = original[['y', 'x', 'w', 'z']]
    tm.assert_frame_equal(original, df)