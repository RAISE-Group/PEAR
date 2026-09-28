@pytest.mark.parametrize('input', [[1, 2, 3], (1, 2, 3), list(range(3)), pd.Categorical(['a', 'b', 'a']), (i for i in range(3)), map(lambda x: x, range(3))])
def test_constructor_index_mismatch(self, input):
    msg = 'Length of passed values is 3, index implies 4'
    with pytest.raises(ValueError, match=msg):
        Series(input, index=np.arange(4))