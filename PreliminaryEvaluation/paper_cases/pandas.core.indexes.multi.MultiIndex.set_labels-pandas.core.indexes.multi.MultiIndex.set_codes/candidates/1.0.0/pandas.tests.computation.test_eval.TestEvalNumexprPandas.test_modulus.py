def test_modulus(self):
    for lhs, rhs in product(self.lhses, self.rhses):
        self.check_modulus(lhs, '%', rhs)