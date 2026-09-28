def test_any_all_object(self):
    result = np.all(DataFrame(columns=['a', 'b'])).item()
    assert result is True
    result = np.any(DataFrame(columns=['a', 'b'])).item()
    assert result is False