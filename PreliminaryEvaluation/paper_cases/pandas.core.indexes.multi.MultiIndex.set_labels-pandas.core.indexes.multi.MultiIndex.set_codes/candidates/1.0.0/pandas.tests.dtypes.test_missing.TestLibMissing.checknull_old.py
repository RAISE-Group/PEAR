def checknull_old(self):
    for value in na_vals:
        assert libmissing.checknull_old(value)
    for value in inf_vals:
        assert libmissing.checknull_old(value)
    for value in int_na_vals:
        assert not libmissing.checknull_old(value)
    for value in sometimes_na_vals:
        assert not libmissing.checknull_old(value)
    for value in never_na_vals:
        assert not libmissing.checknull_old(value)