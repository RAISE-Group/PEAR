def check_alignment(self, result, nlhs, ghs, op):
    try:
        nlhs, ghs = nlhs.align(ghs)
    except (ValueError, TypeError, AttributeError):
        pass
    else:
        expected = self.ne.evaluate(f'nlhs {op} ghs')
        tm.assert_numpy_array_equal(result.values, expected)