@pytest.mark.parametrize('X', [1, [1], [1, 2], [[1], 2], 'a', ['a'], ['a', 'b'], [['a'], 'b']])
def test_invalid_input(self, X):
    msg = 'Input must be a list-like of list-likes'
    with pytest.raises(TypeError, match=msg):
        cartesian_product(X=X)