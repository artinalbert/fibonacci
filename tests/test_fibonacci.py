from fibonacci.fibonacci import fibonacci_loop


def test_fibonacci_loop():
    assert fibonacci_loop(5) == [0, 1, 1, 2, 3]