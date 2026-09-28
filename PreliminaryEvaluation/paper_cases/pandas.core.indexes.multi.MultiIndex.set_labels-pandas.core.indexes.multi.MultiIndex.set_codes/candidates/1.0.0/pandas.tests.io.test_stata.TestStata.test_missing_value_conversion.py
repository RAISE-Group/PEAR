@pytest.mark.parametrize('file', ['dta17_113', 'dta17_115', 'dta17_117'])
def test_missing_value_conversion(self, file):
    columns = ['int8_', 'int16_', 'int32_', 'float32_', 'float64_']
    smv = StataMissingValue(101)
    keys = sorted(smv.MISSING_VALUES.keys())
    data = []
    for i in range(27):
        row = [StataMissingValue(keys[i + j * 27]) for j in range(5)]
        data.append(row)
    expected = DataFrame(data, columns=columns)
    parsed = read_stata(getattr(self, file), convert_missing=True)
    tm.assert_frame_equal(parsed, expected)