def test_hide_single_index(self):
    ctx = self.df.style._translate()
    assert ctx['body'][0][0]['is_visible']
    assert ctx['head'][0][0]['is_visible']
    ctx2 = self.df.style.hide_index()._translate()
    assert not ctx2['body'][0][0]['is_visible']
    assert not ctx2['head'][0][0]['is_visible']
    ctx3 = self.df.set_index('A').style._translate()
    assert ctx3['body'][0][0]['is_visible']
    assert len(ctx3['head']) == 2
    assert ctx3['head'][0][0]['is_visible']
    ctx4 = self.df.set_index('A').style.hide_index()._translate()
    assert not ctx4['body'][0][0]['is_visible']
    assert len(ctx4['head']) == 1
    assert not ctx4['head'][0][0]['is_visible']