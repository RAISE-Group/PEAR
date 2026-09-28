@pytest.mark.slow
def test_unstack_number_of_levels_larger_than_int32(self):
    df = DataFrame(np.random.randn(2 ** 16, 2), index=[np.arange(2 ** 16), np.arange(2 ** 16)])
    with pytest.raises(ValueError, match='int32 overflow'):
        df.unstack()