@pytest.mark.parametrize('norm_cases', normalize_cases)
def test_normalize(self, norm_cases):
    offset, cases = norm_cases
    for dt, expected in cases.items():
        assert offset.apply(dt) == expected