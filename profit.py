""" Lab 2.1 Python Development Exercises

You work for a manufacturer, and have been asked to calculate the total
profit made on the sales of a product. You are given a dictionary containing
the cost price per unit (in dollars), sell price per unit (in dollars), and
the starting inventory. Return the total profit made, rounded to the nearest
dollar.

Examples
profit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}) ➞ 14796

profit({
    "cost_price": 225.89,
    "sell_price": 550.00,
    "inventory": 100
}) ➞ 32411

profit({
    "cost_price": 2.77,
    "sell_price": 7.95,
    "inventory": 8500
}) ➞ 44030

Notes
- Assume all inventory has been sold.
- Profit = Total Sales - Total Cost

:authors: - Hugo Rodríguez
"""

from utils import require


def require_dictionary_keys_exist(d: dict, *key_args):
    for k in key_args:
        require(k in d, f"'{k}' data is missing from dictionary")


def require_dictionary_value_type(d: dict, k: any, t):
    require(
        isinstance(d[k], t),
        f"Expected a '{t.__name__}', '{type(d[k]).__name__}' given"
    )


def profit(d: dict[str, any]) -> int:
    require(
        isinstance(d, dict),
        f"Expected a 'dictionary', '{type(d).__name__}' given"
    )
    require(
        bool(d),
        'Cannot perform profit calculation, empty dictionary given'
    )
    require_dictionary_keys_exist(d, 'sell_price', 'cost_price', 'inventory')
    require_dictionary_value_type(d, 'sell_price', float)
    require_dictionary_value_type(d, 'cost_price', float)
    require_dictionary_value_type(d, 'inventory', int)

    return d['sell_price'] * d['inventory'] - d['cost_price'] * d['inventory']
