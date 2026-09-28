@pytest.mark.parametrize('margin_name', ['foo', 'one', 666, None, ['a', 'b']])
def test_pivot_table_with_margins_set_margin_name(self, margin_name):
    msg = 'Conflicting name "{}" in margins|margins_name argument must be a string'.format(margin_name)
    with pytest.raises(ValueError, match=msg):
        pivot_table(self.data, values='D', index=['A', 'B'], columns=['C'], margins=True, margins_name=margin_name)
    with pytest.raises(ValueError, match=msg):
        pivot_table(self.data, values='D', index=['C'], columns=['A', 'B'], margins=True, margins_name=margin_name)
    with pytest.raises(ValueError, match=msg):
        pivot_table(self.data, values='D', index=['A'], columns=['B'], margins=True, margins_name=margin_name)