@pytest.mark.parametrize('case', on_offset_cases)
def test_is_on_offset(self, case):
    offset, dt, expected = case
    assert_is_on_offset(offset, dt, expected)