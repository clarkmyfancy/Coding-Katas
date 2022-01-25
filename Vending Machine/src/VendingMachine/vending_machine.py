class VendingMachine:

  def consume_coin(self, coin):
    result = ""
    if coin.size == 1 and coin.weight == 1:
      result = "Reject"
    else:
      result = "Accept"
    return result
