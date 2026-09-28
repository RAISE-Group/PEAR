def get_value(self, series, key):
    s = com.values_from_object(series)
    k = com.values_from_object(key)

    def _try_mi(k):
        loc = self.get_loc(k)
        new_values = series._values[loc]
        new_index = self[loc]
        new_index = maybe_droplevels(new_index, k)
        return series._constructor(new_values, index=new_index, name=series.name).__finalize__(self)
    try:
        return self._engine.get_value(s, k)
    except KeyError as e1:
        try:
            return _try_mi(key)
        except KeyError:
            pass
        try:
            return libindex.get_value_at(s, k)
        except IndexError:
            raise
        except TypeError:
            if is_iterator(key):
                raise InvalidIndexError(key)
            else:
                raise e1
        except Exception:
            raise e1
    except TypeError:
        if isinstance(key, (datetime.datetime, np.datetime64, str)):
            try:
                return _try_mi(key)
            except KeyError:
                raise
            except (IndexError, ValueError, TypeError):
                pass
            try:
                return _try_mi(Timestamp(key))
            except (KeyError, TypeError, IndexError, ValueError, tslibs.OutOfBoundsDatetime):
                pass
        raise InvalidIndexError(key)