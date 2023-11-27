import price_info


def test_total_cost_of_shopping():
    result = price_info.total_cost_shopping()
    ans = 46.75
    assert (result == ans)

def test_cost_of_fruit():
    result = price_info.cost_of_fruits('apple', 10)
    ans = 12.0
    assert (result == ans)
