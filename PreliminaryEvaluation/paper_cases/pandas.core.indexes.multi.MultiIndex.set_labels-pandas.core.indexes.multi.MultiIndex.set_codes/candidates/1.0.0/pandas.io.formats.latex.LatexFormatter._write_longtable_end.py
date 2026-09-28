@staticmethod
def _write_longtable_end(buf):
    """
        Write the end of a longtable environment.

        Parameters
        ----------
        buf : string or file handle
            File path or object. If not specified, the result is returned as
            a string.

        """
    buf.write('\\end{longtable}\n')