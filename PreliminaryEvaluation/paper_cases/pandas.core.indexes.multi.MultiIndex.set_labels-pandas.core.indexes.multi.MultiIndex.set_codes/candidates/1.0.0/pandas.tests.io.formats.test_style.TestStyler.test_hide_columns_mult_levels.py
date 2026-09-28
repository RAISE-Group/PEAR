def test_hide_columns_mult_levels(self):
    i1 = pd.MultiIndex.from_arrays([['a', 'a'], [0, 1]], names=['idx_level_0', 'idx_level_1'])
    i2 = pd.MultiIndex.from_arrays([['b', 'b'], [0, 1]], names=['col_level_0', 'col_level_1'])
    df = pd.DataFrame([[1, 2], [3, 4]], index=i1, columns=i2)
    ctx = df.style._translate()
    assert ctx['head'][0][2]['is_visible']
    assert ctx['head'][1][2]['is_visible']
    assert ctx['head'][1][3]['display_value'] == 1
    assert ctx['body'][0][0]['is_visible']
    assert ctx['body'][1][2]['is_visible']
    assert ctx['body'][1][2]['display_value'] == 3
    assert ctx['body'][1][3]['is_visible']
    assert ctx['body'][1][3]['display_value'] == 4
    ctx = df.style.hide_columns('b')._translate()
    assert not ctx['head'][0][2]['is_visible']
    assert not ctx['head'][1][2]['is_visible']
    assert not ctx['body'][1][2]['is_visible']
    assert ctx['body'][0][0]['is_visible']
    ctx = df.style.hide_columns([('b', 0)])._translate()
    assert ctx['head'][0][2]['is_visible']
    assert not ctx['head'][1][2]['is_visible']
    assert not ctx['body'][1][2]['is_visible']
    assert ctx['body'][1][3]['is_visible']
    assert ctx['body'][1][3]['display_value'] == 4
    ctx = df.style.hide_columns([('b', 1)]).hide_index()._translate()
    assert not ctx['body'][0][0]['is_visible']
    assert ctx['head'][0][2]['is_visible']
    assert ctx['head'][1][2]['is_visible']
    assert not ctx['head'][1][3]['is_visible']
    assert not ctx['body'][1][3]['is_visible']
    assert ctx['body'][1][2]['is_visible']
    assert ctx['body'][1][2]['display_value'] == 3