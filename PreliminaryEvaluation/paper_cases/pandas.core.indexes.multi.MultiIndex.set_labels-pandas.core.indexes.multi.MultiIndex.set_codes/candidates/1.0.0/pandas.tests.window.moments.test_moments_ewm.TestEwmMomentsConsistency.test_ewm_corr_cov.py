@pytest.mark.parametrize('name', ['cov', 'corr'])
def test_ewm_corr_cov(self, name, min_periods, binary_ew_data):
    A, B = binary_ew_data
    check_binary_ew(name='corr', A=A, B=B)
    check_binary_ew_min_periods('corr', min_periods, A, B)