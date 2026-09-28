@pytest.mark.parametrize('case', normalize_cases)
def test_normalize(self, case):
    offset, cases = case
    for dt, expected in cases.items():
        assert offset.apply(dt) == expected