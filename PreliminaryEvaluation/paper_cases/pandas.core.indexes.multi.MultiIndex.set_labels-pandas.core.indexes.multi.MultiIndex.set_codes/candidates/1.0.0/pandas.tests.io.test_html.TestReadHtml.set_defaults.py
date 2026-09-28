@pytest.fixture(autouse=True, scope='function')
def set_defaults(self, flavor, request):
    self.read_html = partial(read_html, flavor=flavor)
    yield