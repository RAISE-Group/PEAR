@contextmanager
def run_transaction(self):
    cur = self.con.cursor()
    try:
        yield cur
        self.con.commit()
    except Exception:
        self.con.rollback()
        raise
    finally:
        cur.close()