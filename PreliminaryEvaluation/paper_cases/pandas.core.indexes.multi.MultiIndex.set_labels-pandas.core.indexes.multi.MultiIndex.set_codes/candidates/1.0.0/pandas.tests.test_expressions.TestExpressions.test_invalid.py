def test_invalid(self):
    result = expr._can_use_numexpr(operator.add, None, self.frame, self.frame, 'evaluate')
    assert not result
    result = expr._can_use_numexpr(operator.add, '+', self.mixed, self.frame, 'evaluate')
    assert not result
    result = expr._can_use_numexpr(operator.add, '+', self.frame2, self.frame2, 'evaluate')
    assert not result
    result = expr._can_use_numexpr(operator.add, '+', self.frame, self.frame2, 'evaluate')
    assert result