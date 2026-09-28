def execute(self, *args, **kwargs):
    if self.is_cursor:
        cur = self.con
    else:
        cur = self.con.cursor()
    try:
        cur.execute(*args, **kwargs)
        return cur
    except Exception as exc:
        try:
            self.con.rollback()
        except Exception as inner_exc:
            ex = DatabaseError(f'Execution failed on sql: {args[0]}\n{exc}\nunable to rollback')
            raise ex from inner_exc
        ex = DatabaseError(f"Execution failed on sql '{args[0]}': {exc}")
        raise ex from exc