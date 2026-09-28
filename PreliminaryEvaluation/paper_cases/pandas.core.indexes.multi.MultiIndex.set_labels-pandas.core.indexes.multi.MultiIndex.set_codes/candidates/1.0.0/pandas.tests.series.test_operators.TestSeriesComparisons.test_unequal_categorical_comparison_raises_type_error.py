def test_unequal_categorical_comparison_raises_type_error(self):
    cat = Series(Categorical(list('abc')))
    with pytest.raises(TypeError):
        cat > 'b'
    cat = Series(Categorical(list('abc'), ordered=False))
    with pytest.raises(TypeError):
        cat > 'b'
    cat = Series(Categorical(list('abc'), ordered=True))
    with pytest.raises(TypeError):
        cat < 'd'
    with pytest.raises(TypeError):
        cat > 'd'
    with pytest.raises(TypeError):
        'd' < cat
    with pytest.raises(TypeError):
        'd' > cat
    tm.assert_series_equal(cat == 'd', Series([False, False, False]))
    tm.assert_series_equal(cat != 'd', Series([True, True, True]))