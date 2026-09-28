@pytest.mark.filterwarnings('ignore::PendingDeprecationWarning')
def test_is_scalar_numpy_arrays(self):
    assert not is_scalar(np.array([]))
    assert not is_scalar(np.array([[]]))
    assert not is_scalar(np.matrix('1; 2'))