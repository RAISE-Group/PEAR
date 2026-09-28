def test_to_string_float_format_no_fixed_width(self):
    df = DataFrame({'x': [0.19999]})
    expected = '      x\n0 0.200'
    assert df.to_string(float_format='%.3f') == expected
    df = DataFrame({'x': [100.0]})
    expected = '    x\n0 100'
    assert df.to_string(float_format='%.0f') == expected