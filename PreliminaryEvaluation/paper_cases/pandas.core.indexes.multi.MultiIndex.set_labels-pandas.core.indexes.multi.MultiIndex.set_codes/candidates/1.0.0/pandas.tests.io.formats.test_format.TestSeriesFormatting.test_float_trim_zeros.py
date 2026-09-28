def test_float_trim_zeros(self):
    vals = [20843091730.5, 35220501730.5, 23067481730.5, 20395421730.5, 55989781730.5]
    for line in repr(Series(vals)).split('\n'):
        if line.startswith('dtype:'):
            continue
        if _three_digit_exp():
            assert '+010' in line
        else:
            assert '+10' in line