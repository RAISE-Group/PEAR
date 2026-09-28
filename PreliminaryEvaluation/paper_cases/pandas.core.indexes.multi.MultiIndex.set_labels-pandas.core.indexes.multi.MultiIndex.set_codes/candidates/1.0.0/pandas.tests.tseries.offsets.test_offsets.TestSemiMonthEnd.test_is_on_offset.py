@pytest.mark.parametrize('case', on_offset_cases)
def test_is_on_offset(self, case):
    dt, expected = case
    assert_is_on_offset(SemiMonthEnd(), dt, expected)