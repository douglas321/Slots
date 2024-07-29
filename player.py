class Player:
    def __init__(self,player_id, name) -> None:
        self._name = name
        self._wallet = 100
        self._player_id = player_id

    def add_funds(self, amount):
        self._wallet += amount
    def get_funds(self):
        return(self._wallet)
        
    def get_player_info(self):
        print(f"Name: {self._name}, Wallet: ${self._wallet}, Player ID: {self._player_id}")

    