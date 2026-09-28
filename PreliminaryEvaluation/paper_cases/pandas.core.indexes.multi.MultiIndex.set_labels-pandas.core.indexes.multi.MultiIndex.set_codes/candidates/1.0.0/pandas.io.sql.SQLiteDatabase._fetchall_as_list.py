def _fetchall_as_list(self, cur):
    result = cur.fetchall()
    if not isinstance(result, list):
        result = list(result)
    return result