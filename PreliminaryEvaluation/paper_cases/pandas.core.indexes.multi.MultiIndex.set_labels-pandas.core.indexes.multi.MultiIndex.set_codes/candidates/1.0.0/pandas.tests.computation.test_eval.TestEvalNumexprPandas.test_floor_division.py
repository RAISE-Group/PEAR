def test_floor_division(self):
    for lhs, rhs in product(self.lhses, self.rhses):
        self.check_floor_division(lhs, '//', rhs)