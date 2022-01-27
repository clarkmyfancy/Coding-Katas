import unittest
from unittest.mock import patch

from src.VendingMachine.vending_machine import VendingMachine

class TestVendingMachine(unittest.TestCase):

    @patch("src.Coin.coin.Coin")
    def test_should_reject_invalid_coins(self, mocked_coin):
        penny = mocked_coin()
        penny.size = 1
        penny.weight = 1
        
        failure_message = "Pennies should have been rejected"
        self.assertEqual("Reject", VendingMachine().consume_coin(penny), failure_message)

    @patch("src.Coin.coin.Coin")
    def test_should_accept_valid_quarters(self, mocked_coin):
        quarter = mocked_coin()
        quarter.size = 3
        quarter.weight = 3

        msg = "Quarter should have been accepted"
        self.assertEqual("Accept", VendingMachine().consume_coin(quarter), msg)

    @patch("src.Coin.coin.Coin")
    def test_should_accept_valid_dimes(self, mocked_coin):
        dime = mocked_coin()
        dime.size = .5
        dime.weight = .5
        msg = "Dime should have been accepted"
        self.assertEqual("Accept", VendingMachine().consume_coin(dime), msg)

    @patch("src.Coin.coin.Coin")
    def test_should_accept_valid_nickles(self, mocked_coin):
        nickle = mocked_coin()
        nickle.size = 1
        nickle.weight = .5

        msg = "Nickle should have been accepted"
        self.assertEqual("Accept", VendingMachine().consume_coin(nickle), msg)

    @patch("src.Coin.coin.Coin")
    def test_should_put_rejected_coins_into_coin_return_slot(self, mocked_coin):

        v = VendingMachine()
        for _ in range(4):
            penny = mocked_coin()
            penny.size = 1
            penny.weight = 1
            v.consume_coin(penny)

        msg = "The inserted pennies were not rejected"
        self.assertEqual(4, len(v.get_contents_of_coin_return_slot()), msg)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
