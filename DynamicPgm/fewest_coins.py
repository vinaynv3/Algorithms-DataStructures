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

def CoinChangeRecursion(amount,coin_list):

    amount = int(amount)
    if amount == 0:
        return 0

    else:
        return amount // coin_list[0] +  CoinChangeRecursion(amount % coin_list[0],coin_list[1:])


def main():
    #print(CoinChange(sys.argv[-1]))
    print(CoinChangeRecursion(sys.argv[-1],[25,10,5,1]))

if __name__ == "__main__":

    main()



