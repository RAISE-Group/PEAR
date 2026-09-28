@pytest.mark.parametrize('type', [int, float])
def test_fillna_positive_limit(self, type):
    df = DataFrame(np.random.randn(10, 4)).astype(type)
    msg = 'Limit must be greater than 0'
    with pytest.raises(ValueError, match=msg):
        df.fillna(0, limit=-5)