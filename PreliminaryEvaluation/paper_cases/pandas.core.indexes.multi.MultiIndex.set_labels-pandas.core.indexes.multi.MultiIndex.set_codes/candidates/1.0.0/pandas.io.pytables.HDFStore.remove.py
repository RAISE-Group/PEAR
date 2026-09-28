def remove(self, key: str, where=None, start=None, stop=None):
    """
        Remove pandas object partially by specifying the where condition

        Parameters
        ----------
        key : string
            Node to remove or delete rows from
        where : list of Term (or convertible) objects, optional
        start : integer (defaults to None), row number to start selection
        stop  : integer (defaults to None), row number to stop selection

        Returns
        -------
        number of rows removed (or None if not a Table)

        Raises
        ------
        raises KeyError if key is not a valid store

        """
    where = _ensure_term(where, scope_level=1)
    try:
        s = self.get_storer(key)
    except KeyError:
        raise
    except AssertionError:
        raise
    except Exception:
        if where is not None:
            raise ValueError('trying to remove a node with a non-None where clause!')
        node = self.get_node(key)
        if node is not None:
            node._f_remove(recursive=True)
            return None
    if com.all_none(where, start, stop):
        s.group._f_remove(recursive=True)
    else:
        if not s.is_table:
            raise ValueError('can only remove with where on objects written as tables')
        return s.delete(where=where, start=start, stop=stop)