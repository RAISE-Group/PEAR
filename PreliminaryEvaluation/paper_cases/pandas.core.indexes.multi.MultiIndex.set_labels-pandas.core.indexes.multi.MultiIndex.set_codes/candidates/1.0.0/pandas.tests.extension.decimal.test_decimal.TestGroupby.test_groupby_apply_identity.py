@pytest.mark.xfail(reason='needs to correctly define __eq__ to handle nans, xref #27081.')
def test_groupby_apply_identity(self, data_for_grouping):
    super().test_groupby_apply_identity(data_for_grouping)