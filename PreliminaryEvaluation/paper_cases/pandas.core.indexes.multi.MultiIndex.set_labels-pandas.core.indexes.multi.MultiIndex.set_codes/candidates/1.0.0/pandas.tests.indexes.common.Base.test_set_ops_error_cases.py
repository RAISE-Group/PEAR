@pytest.mark.parametrize('case', [0.5, 'xxx'])
@pytest.mark.parametrize('method', ['intersection', 'union', 'difference', 'symmetric_difference'])
def test_set_ops_error_cases(self, case, method, indices):
    msg = 'Input must be Index or array-like'
    with pytest.raises(TypeError, match=msg):
        getattr(indices, method)(case)