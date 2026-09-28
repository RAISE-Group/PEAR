@contextmanager
def run_transaction(self):
    with self.connectable.begin() as tx:
        if hasattr(tx, 'execute'):
            yield tx
        else:
            yield self.connectable