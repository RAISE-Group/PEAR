def test_hide_columns_single_level(self):
    ctx = self.df.style._translate()
    assert ctx['head'][0][1]['is_visible']
    assert ctx['head'][0][1]['display_value'] == 'A'
    assert ctx['head'][0][2]['is_visible']
    assert ctx['head'][0][2]['display_value'] == 'B'
    assert ctx['body'][0][1]['is_visible']
    assert ctx['body'][1][2]['is_visible']
    ctx = self.df.style.hide_columns('A')._translate()
    assert not ctx['head'][0][1]['is_visible']
    assert not ctx['body'][0][1]['is_visible']
    assert ctx['body'][1][2]['is_visible']
    ctx = self.df.style.hide_columns(['A', 'B'])._translate()
    assert not ctx['head'][0][1]['is_visible']
    assert not ctx['head'][0][2]['is_visible']
    assert not ctx['body'][0][1]['is_visible']
    assert not ctx['body'][1][2]['is_visible']