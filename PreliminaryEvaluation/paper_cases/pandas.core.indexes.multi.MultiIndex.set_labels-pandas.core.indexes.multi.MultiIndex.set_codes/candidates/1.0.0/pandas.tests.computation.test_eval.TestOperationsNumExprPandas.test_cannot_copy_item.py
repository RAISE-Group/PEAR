@pytest.mark.parametrize('invalid_target', [1, 'cat', (1, 3)])
def test_cannot_copy_item(self, invalid_target):
    msg = 'Cannot return a copy of the target'
    expression = 'a = 1 + 2'
    with pytest.raises(ValueError, match=msg):
        self.eval(expression, target=invalid_target, inplace=False)