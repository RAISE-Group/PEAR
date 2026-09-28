def test_stack_multiple_out_of_bounds(self):
    unstacked = self.ymd.unstack(['year', 'month'])
    with pytest.raises(IndexError, match='Too many levels'):
        unstacked.stack([2, 3])
    with pytest.raises(IndexError, match='not a valid level number'):
        unstacked.stack([-4, -3])