@pytest.mark.parametrize('invalid', [345600000000000, 'a'])
def test_td64_comparisons_invalid(self, box_with_array, invalid):
    box = box_with_array
    rng = timedelta_range('1 days', periods=10)
    obj = tm.box_expected(rng, box)
    assert_invalid_comparison(obj, invalid, box)