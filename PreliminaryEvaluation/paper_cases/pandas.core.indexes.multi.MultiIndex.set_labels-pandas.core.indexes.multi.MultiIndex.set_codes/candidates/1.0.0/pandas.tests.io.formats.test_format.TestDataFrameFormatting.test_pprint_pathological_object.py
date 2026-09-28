def test_pprint_pathological_object(self):
    """
        If the test fails, it at least won't hang.
        """

    class A:

        def __getitem__(self, key):
            return 3
    df = DataFrame([A()])
    repr(df)