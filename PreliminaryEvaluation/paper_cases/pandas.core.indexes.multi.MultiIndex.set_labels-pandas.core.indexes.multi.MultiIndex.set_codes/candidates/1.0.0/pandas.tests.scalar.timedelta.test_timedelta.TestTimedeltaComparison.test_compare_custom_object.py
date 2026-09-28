@pytest.mark.skip(reason='GH#20829 is reverted until after 0.24.0')
def test_compare_custom_object(self):
    """
        Make sure non supported operations on Timedelta returns NonImplemented
        and yields to other operand (GH#20829).
        """

    class CustomClass:

        def __init__(self, cmp_result=None):
            self.cmp_result = cmp_result

        def generic_result(self):
            if self.cmp_result is None:
                return NotImplemented
            else:
                return self.cmp_result

        def __eq__(self, other):
            return self.generic_result()

        def __gt__(self, other):
            return self.generic_result()
    t = Timedelta('1s')
    assert not t == 'string'
    assert not t == 1
    assert not t == CustomClass()
    assert not t == CustomClass(cmp_result=False)
    assert t < CustomClass(cmp_result=True)
    assert not t < CustomClass(cmp_result=False)
    assert t == CustomClass(cmp_result=True)