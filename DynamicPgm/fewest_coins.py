"""
Below program returns few coins in change of a given bill
Strategy: Dynamic programming

"""
import sys

def CoinChange(coin):

    coins = [25,10,5,1]
    total_coins = 0
    coins_position = 0

    while int(coin) > 0 and coins_position < len(coins):
        
        total_coins += int(coin) // coins[coins_position]
        coin = int(coin) % coins[coins_position]

        coins_position +=1

    return total_coins

def main():
    print(CoinChange(sys.argv[-1]))

if __name__ == "__main__":

    main()



