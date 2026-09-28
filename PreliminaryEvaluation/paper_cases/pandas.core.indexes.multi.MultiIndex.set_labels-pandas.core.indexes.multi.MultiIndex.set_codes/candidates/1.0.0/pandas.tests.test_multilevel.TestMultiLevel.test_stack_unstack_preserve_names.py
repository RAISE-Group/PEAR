def test_stack_unstack_preserve_names(self):
    unstacked = self.frame.unstack()
    assert unstacked.index.name == 'first'
    assert unstacked.columns.names == ['exp', 'second']
    restacked = unstacked.stack()
    assert restacked.index.names == self.frame.index.names