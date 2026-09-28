@pytest.mark.parametrize('name', ['cov', 'corr'])
def test_different_input_array_raise_exception(self, name, binary_ew_data):
    A, _ = binary_ew_data
    msg = 'Input arrays must be of the same type!'
    with pytest.raises(Exception, match=msg):
        ew_func(A, randn(50), 20, name=name, min_periods=5)