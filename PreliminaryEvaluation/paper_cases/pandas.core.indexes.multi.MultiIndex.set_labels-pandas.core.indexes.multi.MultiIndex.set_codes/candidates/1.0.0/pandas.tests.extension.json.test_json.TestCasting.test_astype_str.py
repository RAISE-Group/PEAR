@pytest.mark.skip(reason='failing on np.array(self, dtype=str)')
def test_astype_str(self):
    """This currently fails in NumPy on np.array(self, dtype=str) with

        *** ValueError: setting an array element with a sequence
        """