def check_alignment(self, result, nlhs, ghs, op):
    try:
        nlhs, ghs = nlhs.align(ghs)
    except (ValueError, TypeError, AttributeError):
        pass
    else:
        expected = eval(f'nlhs {op} ghs')
        tm.assert_almost_equal(result, expected)