""" Lab 2.1 Python Development Exercises

You work for a manufacturer, and have been asked to calculate the total profit made on the
sales of a product. You are given a dictionary containing the cost price per unit (in
dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made,
rounded to the nearest dollar.

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

"""
Test Cases:

1- [TTP] Get profit
2- [TTF] Pass empty dictionary
3- [TTF] Pass dictionary with invalid keys
4- [TTP] Dictionary with extra keys
5- [TTF] Pass any other type
6- [TTF] Pass None
7- [TTF] Pass dictionary with None as values
8- [TTP] Dictionary values as other data types
"""

import unittest

def checkArgument(expression: bool, errorMsg: str):
    if not expression:
        raise ValueError(errorMsg)

def checkDictionaryKeysExist(d: dict, *key_args):
    for k in key_args:
        checkArgument(k in d, f"'{k}' data is missing from dictionary")

def checkDictionaryValueType(d: dict, k: any, t):
    checkArgument(isinstance(d[k], t), f"Expected a '{t.__name__}', '{type(d[k]).__name__}' given")

def profit(d: dict[str, any]) -> int:
    checkArgument(isinstance(d, dict), f"Expected a 'dictionary', '{type(d).__name__}' given")
    checkArgument(bool(d), 'Cannot perform profit calculation, empty dictionary given')
    checkDictionaryKeysExist(d, 'sell_price', 'cost_price', 'inventory')
    checkDictionaryValueType(d, 'sell_price', float)
    checkDictionaryValueType(d, 'cost_price', float)
    checkDictionaryValueType(d, 'inventory', int)
    
    return d['sell_price'] * d['inventory'] - d['cost_price'] * d['inventory']

class ProfitTest(unittest.TestCase):
    def test_pass_get_correct_profit(self):
        self.assertAlmostEqual(14796, profit({
            'cost_price': 32.67,
            'sell_price': 45.00,
            'inventory': 1200
        }))
        self.assertAlmostEqual(32411, profit({
            'cost_price': 225.89,
            'sell_price': 550.00,
            'inventory': 100
        }))

    def test_fail_empty_dictionary_given(self):
        with self.assertRaises(ValueError):
            profit({})

    def test_fail_dict_with_invalid_keys(self):
        with self.assertRaises(ValueError):
            profit({
                'price_cost': 225.89,
                'price_sell': 145.00,
                'stock': 8500
            })

        with self.assertRaises(ValueError):
            profit({
                'sell_price': 225.89,
                'price_sell': 145.00,
                'stock': 8500
            })

        with self.assertRaises(ValueError):
            profit({
                'sell_price': 225.89,
                'cost_price': 145.00,
                'stock': 8500
            })

    def test_pass_dict_with_extra_keys(self):
        self.assertAlmostEqual(44030, profit({
            'cost_price': 2.77,
            'sell_price': 7.95,
            'location': 'warehouse',
            'inventory': 8500,
            'company_name': 'tuxtech',
            'origin_country': 'mx',
        }))

    def test_fail_passed_arg_is_not_a_dict(self):
        with self.assertRaises(ValueError):
            profit(('cost_price', 2.77, 'sell_price', 7.95, 'inventory', 8500))

        with self.assertRaises(ValueError):
            profit(['cost_price', 2.77, 'sell_price', 7.95, 'inventory', 8500])

    def test_fail_passed_arg_is_none(self):
        with self.assertRaises(ValueError):
            profit(None)

    def test_fail_passed_dict_inner_values_are_none(self):
        with self.assertRaises(ValueError):
            profit({
                'cost_price': None,
                'sell_price': None,
                'inventory': None,
            })

    def test_fail_passed_dict_inner_keys_wrong_types(self):
        with self.assertRaises(ValueError):
            profit({
                'price_cost': '225.89',
                'price_sell': 145j,
                'stock': 8500.1
            })

        with self.assertRaises(ValueError):
            profit({
                'sell_price': 225.89,
                'price_sell': 145j,
                'stock': 8500.1
            })

        with self.assertRaises(ValueError):
            profit({
                'sell_price': 225.89,
                'cost_price': 145.00,
                'stock': 8500.1
            })

if __name__ == "__main__":
    unittest.main()
