@pytest.mark.parametrize('invalid_target', [1, 'cat', [1, 2], np.array([]), (1, 3)])
@pytest.mark.filterwarnings('ignore::FutureWarning')
def test_cannot_item_assign(self, invalid_target):
    msg = 'Cannot assign expression output to target'
    expression = 'a = 1 + 2'
    with pytest.raises(ValueError, match=msg):
        self.eval(expression, target=invalid_target, inplace=True)
    if hasattr(invalid_target, 'copy'):
        with pytest.raises(ValueError, match=msg):
            self.eval(expression, target=invalid_target, inplace=False)