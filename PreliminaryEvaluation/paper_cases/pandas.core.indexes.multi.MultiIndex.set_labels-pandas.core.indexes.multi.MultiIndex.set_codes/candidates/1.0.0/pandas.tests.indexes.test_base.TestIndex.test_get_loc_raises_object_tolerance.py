def test_get_loc_raises_object_tolerance(self):
    index = pd.Index(['a', 'c'])
    with pytest.raises(TypeError, match='unsupported operand type'):
        index.get_loc('a', method='pad', tolerance='invalid')