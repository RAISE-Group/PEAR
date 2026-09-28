@pytest.mark.parametrize('case', on_offset_cases)
def test_is_on_offset(self, case):
    offset, cases = case
    for dt, expected in cases.items():
        assert offset.is_on_offset(dt) == expected