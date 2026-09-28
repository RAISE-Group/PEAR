@pytest.mark.parametrize('case', offset_cases)
def test_offset(self, case):
    offset, cases = case
    for base, expected in cases.items():
        assert_offset_equal(offset, base, expected)