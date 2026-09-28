@pytest.mark.parametrize('case', apply_large_n_cases)
def test_apply_large_n(self, case):
    offset, cases = case
    for base, expected in cases.items():
        assert_offset_equal(offset, base, expected)