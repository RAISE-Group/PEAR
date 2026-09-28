@td.skip_if_windows
def test_result_complex128(self):
    self.check_result_type(np.complex128, np.complex128)