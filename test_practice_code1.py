def test_add():
    from practice_code1 import add
    expected = 3
    a = 1
    b = 2
    answer = add(a, b)
    assert expected == answer


def test_divide():
    from practice_code1 import divide
    expected = 5
    a = 10
    b = 2
    answer = divide(a, b)
    assert  expected == answer