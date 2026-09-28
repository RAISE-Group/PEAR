def test_ismethods(self):
    values = ['A', 'b', 'Xy', '4', '3A', '', 'TT', '55', '-', '  ']
    str_s = Series(values)
    alnum_e = [True, True, True, True, True, False, True, True, False, False]
    alpha_e = [True, True, True, False, False, False, True, False, False, False]
    digit_e = [False, False, False, True, False, False, False, True, False, False]
    num_e = [False, False, False, True, False, False, False, True, False, False]
    space_e = [False, False, False, False, False, False, False, False, False, True]
    lower_e = [False, True, False, False, False, False, False, False, False, False]
    upper_e = [True, False, False, False, True, False, True, False, False, False]
    title_e = [True, False, True, False, True, False, False, False, False, False]
    tm.assert_series_equal(str_s.str.isalnum(), Series(alnum_e))
    tm.assert_series_equal(str_s.str.isalpha(), Series(alpha_e))
    tm.assert_series_equal(str_s.str.isdigit(), Series(digit_e))
    tm.assert_series_equal(str_s.str.isspace(), Series(space_e))
    tm.assert_series_equal(str_s.str.islower(), Series(lower_e))
    tm.assert_series_equal(str_s.str.isupper(), Series(upper_e))
    tm.assert_series_equal(str_s.str.istitle(), Series(title_e))
    assert str_s.str.isalnum().tolist() == [v.isalnum() for v in values]
    assert str_s.str.isalpha().tolist() == [v.isalpha() for v in values]
    assert str_s.str.isdigit().tolist() == [v.isdigit() for v in values]
    assert str_s.str.isspace().tolist() == [v.isspace() for v in values]
    assert str_s.str.islower().tolist() == [v.islower() for v in values]
    assert str_s.str.isupper().tolist() == [v.isupper() for v in values]
    assert str_s.str.istitle().tolist() == [v.istitle() for v in values]