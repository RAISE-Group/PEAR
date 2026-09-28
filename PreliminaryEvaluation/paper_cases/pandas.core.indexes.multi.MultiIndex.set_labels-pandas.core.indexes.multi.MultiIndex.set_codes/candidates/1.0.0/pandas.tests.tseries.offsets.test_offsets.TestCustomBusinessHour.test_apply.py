@pytest.mark.parametrize('apply_case', apply_cases)
def test_apply(self, apply_case):
    offset, cases = apply_case
    for base, expected in cases.items():
        assert_offset_equal(offset, base, expected)