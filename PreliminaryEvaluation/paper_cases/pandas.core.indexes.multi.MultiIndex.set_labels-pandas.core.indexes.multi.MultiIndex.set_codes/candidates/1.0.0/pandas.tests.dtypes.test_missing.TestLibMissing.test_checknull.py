def test_checknull(self):
    for value in na_vals:
        assert libmissing.checknull(value)
    for value in inf_vals:
        assert not libmissing.checknull(value)
    for value in int_na_vals:
        assert not libmissing.checknull(value)
    for value in sometimes_na_vals:
        assert not libmissing.checknull(value)
    for value in never_na_vals:
        assert not libmissing.checknull(value)