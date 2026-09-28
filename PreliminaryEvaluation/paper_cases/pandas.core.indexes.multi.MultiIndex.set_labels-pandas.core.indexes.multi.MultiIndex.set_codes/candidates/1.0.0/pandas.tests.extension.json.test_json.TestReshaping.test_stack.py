@pytest.mark.skip(reason='Different definitions of NA')
def test_stack(self):
    """
        The test does .astype(object).stack(). If we happen to have
        any missing values in `data`, then we'll end up with different
        rows since we consider `{}` NA, but `.astype(object)` doesn't.
        """