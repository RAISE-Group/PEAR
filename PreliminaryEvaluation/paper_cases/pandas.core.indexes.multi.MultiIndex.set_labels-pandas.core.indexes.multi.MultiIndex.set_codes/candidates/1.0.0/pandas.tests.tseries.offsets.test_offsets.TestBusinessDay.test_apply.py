@pytest.mark.parametrize('case', apply_cases)
def test_apply(self, case):
    offset, cases = case
    for base, expected in cases.items():
        assert_offset_equal(offset, base, expected)