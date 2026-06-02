def valid_mark(mark):

    try:

        mark = float(mark)

        if 0 <= mark <= 100:

            return True

        return False

    except ValueError:

        return False
