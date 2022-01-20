from solutions import one

SOLUTIONS_DICT = {
    one: 233168
}


def test_all():

    for key, val in SOLUTIONS_DICT.items():
        assert key.solution == val
