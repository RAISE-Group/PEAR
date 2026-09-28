def test_read_dta12(self):
    parsed_117 = self.read_dta(self.dta21_117)
    expected = DataFrame.from_records([[1, 'abc', 'abcdefghi'], [3, 'cba', 'qwertywertyqwerty'], [93, '', 'strl']], columns=['x', 'y', 'z'])
    tm.assert_frame_equal(parsed_117, expected, check_dtype=False)