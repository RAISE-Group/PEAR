@pytest.mark.parametrize('target', [1, 'cat', [1, 2], np.array([]), (1, 3), {1: 2}])
def test_inplace_no_assignment(self, target):
    expression = '1 + 2'
    assert self.eval(expression, target=target, inplace=False) == 3
    msg = 'Cannot operate inplace if there is no assignment'
    with pytest.raises(ValueError, match=msg):
        self.eval(expression, target=target, inplace=True)