@pytest.mark.parametrize('nano_case', nano_cases)
def test_apply_nanoseconds(self, nano_case):
    offset, cases = nano_case
    for base, expected in cases.items():
        assert_offset_equal(offset, base, expected)