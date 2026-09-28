def test_constructor_name_unhashable(self):
    msg = 'Series\\.name must be a hashable type'
    for n in [['name_list'], np.ones(2), {1: 2}]:
        for data in [['name_list'], np.ones(2), {1: 2}]:
            with pytest.raises(TypeError, match=msg):
                Series(data, name=n)