def test_astype_object(self):
    rng = date_range('1/1/2000', periods=20)
    casted = rng.astype('O')
    exp_values = list(rng)
    tm.assert_index_equal(casted, Index(exp_values, dtype=np.object_))
    assert casted.tolist() == exp_values