def test_stack_names_and_numbers(self):
    unstacked = self.ymd.unstack(['year', 'month'])
    with pytest.raises(ValueError, match='level should contain'):
        unstacked.stack([0, 'month'])