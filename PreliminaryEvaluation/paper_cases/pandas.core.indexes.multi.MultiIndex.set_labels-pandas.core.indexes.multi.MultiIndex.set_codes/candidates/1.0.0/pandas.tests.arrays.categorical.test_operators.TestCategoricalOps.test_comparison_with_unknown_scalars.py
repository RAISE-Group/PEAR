def test_comparison_with_unknown_scalars(self):
    cat = Categorical([1, 2, 3], ordered=True)
    msg = 'Cannot compare a Categorical for op __{}__ with a scalar, which is not a category'
    with pytest.raises(TypeError, match=msg.format('lt')):
        cat < 4
    with pytest.raises(TypeError, match=msg.format('gt')):
        cat > 4
    with pytest.raises(TypeError, match=msg.format('gt')):
        4 < cat
    with pytest.raises(TypeError, match=msg.format('lt')):
        4 > cat
    tm.assert_numpy_array_equal(cat == 4, np.array([False, False, False]))
    tm.assert_numpy_array_equal(cat != 4, np.array([True, True, True]))