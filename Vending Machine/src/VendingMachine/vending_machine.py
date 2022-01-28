class VendingMachine:

  def __init__(self):
    self.coin_return_slot = []
    self.session_wallet = {
      "Quarters": 0,
      "Dimes": 0,
      "Nickles": 0
    }

  def consume_coin(self, coin):
    result = ""
    if self.is_valid(coin):
      result = "Accept"
      self.add_to_session_wallet(coin)
    else:
      result = "Reject"
      self.coin_return_slot.append(coin)
      
    return result

  def is_valid(self, coin):
    coin_is_a_quarter = self.is_a_quarter(coin)
    coin_is_a_dime = self.is_a_dime(coin)
    coin_is_a_nickle = self.is_a_nickle(coin)
    if coin_is_a_quarter or coin_is_a_dime or coin_is_a_nickle:
      return True
    else: 
      return False

  def is_a_quarter(self, coin):
    return True if coin.size == 3 and coin.weight == 3 else False

  def is_a_dime(self, coin):
    return True if coin.size == .5 and coin.weight == .5 else False

  def is_a_nickle(self, coin):
    return True if coin.size == 1 and coin.weight == .5 else False

  def add_to_session_wallet(self, coin):
    if self.is_a_quarter(coin):
      self.session_wallet["Quarters"] += 1
    elif self.is_a_dime(coin):
      self.session_wallet["Dimes"] += 1
    else:
      self.session_wallet["Nickles"] += 1

  def get_contents_of_coin_return_slot(self):
    return self.coin_return_slot

  def get_contents_of_session_wallet(self):
    return self.session_wallet

  def get_number_of_coins_in_session_wallet(self):
    count = 0
    for key in self.session_wallet:
      count += self.session_wallet[key]
    return count
