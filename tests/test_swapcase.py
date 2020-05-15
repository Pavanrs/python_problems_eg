from programs.hackerrank.swapcase import swap_case


def test_case1_swap_case():
    str_input = "Hello"
    str_expected = "hELLO"
    str_actual = swap_case(str_input)

    assert str_expected == str_actual


def test_case2_swap_case():
    str_input = "123456"
    str_expected = "123456"
    str_actual = swap_case(str_input)

    assert str_expected == str_actual


def test_case3_swap_case():
    str_input = None
    str_expected = None
    str_actual = swap_case(str_input)

    assert str_expected == str_actual
