from fibonacci.loops import main


def test_main():
    assert main() == {2: 'a', 3: 'b', 4: 'c', 5: 'd', 6: 'e', 0: 'f', 8: 'f'}
