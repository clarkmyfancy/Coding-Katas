class VendingMachine:

  coin_return_slot = []
  virtual_wallet = []

  def __init__(self):
    self.coin_return_slot = []
    self.session_wallet = []

  def consume_coin(self, coin):
    result = ""
    if coin.size == 1 and coin.weight == 1:
      result = "Reject"
      self.coin_return_slot.append(coin)
    else:
      result = "Accept"
      self.session_wallet.append(coin)
    return result


  def get_contents_of_coin_return_slot(self):
    return self.coin_return_slot

  def get_contents_of_session_wallet(self):
    return self.session_wallet
