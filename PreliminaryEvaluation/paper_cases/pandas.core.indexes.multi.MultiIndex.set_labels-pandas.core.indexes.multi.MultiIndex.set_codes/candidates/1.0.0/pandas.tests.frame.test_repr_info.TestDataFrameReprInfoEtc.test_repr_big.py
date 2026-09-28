@pytest.mark.slow
def test_repr_big(self):
    biggie = DataFrame(np.zeros((200, 4)), columns=range(4), index=range(200))
    repr(biggie)