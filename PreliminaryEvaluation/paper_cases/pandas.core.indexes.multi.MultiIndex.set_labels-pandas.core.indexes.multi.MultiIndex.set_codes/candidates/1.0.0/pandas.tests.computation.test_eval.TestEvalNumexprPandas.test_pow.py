@td.skip_if_windows
def test_pow(self):
    for lhs, rhs in product(self.lhses, self.rhses):
        self.check_pow(lhs, '**', rhs)