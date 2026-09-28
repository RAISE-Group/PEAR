def test_parr_add_iadd_parr_raises(self, box_with_array):
    rng = pd.period_range('1/1/2000', freq='D', periods=5)
    other = pd.period_range('1/6/2000', freq='D', periods=5)
    rng = tm.box_expected(rng, box_with_array)
    with pytest.raises(TypeError):
        rng + other
    with pytest.raises(TypeError):
        rng += other