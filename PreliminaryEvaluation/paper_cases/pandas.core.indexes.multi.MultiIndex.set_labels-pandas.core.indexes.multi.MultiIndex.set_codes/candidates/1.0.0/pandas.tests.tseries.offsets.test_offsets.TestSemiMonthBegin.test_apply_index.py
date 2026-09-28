@pytest.mark.parametrize('case', offset_cases)
def test_apply_index(self, case):
    offset, cases = case
    s = DatetimeIndex(cases.keys())
    with tm.assert_produces_warning(None):
        result = offset.apply_index(s)
    exp = DatetimeIndex(cases.values())
    tm.assert_index_equal(result, exp)