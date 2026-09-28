def test_repr_max_rows(self):
    with pd.option_context('max_rows', None):
        str(Series(range(1001)))