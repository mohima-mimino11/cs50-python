"""
Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

    Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛
    , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
    Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

    import requests

    try:
        ...
    except requests.RequestException:
        ...

    Outputs the current cost of 𝑛
    Bitcoins in USD to four decimal places, using , as a thousands separator.

Hints

    Recall that the sys module comes with argv, per docs.python.org/3/library/sys.html#sys.argv.
    Note that the requests module comes with quite a few methods, per requests.readthedocs.io/en/latest, among which are get, per requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request, and json, per requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content. You can install it with:

    pip install requests

    Note that CoinCap’s API returns a JSON response like:

    {
      "data": {
        "id": "bitcoin",
        "rank": "1",
        "symbol": "BTC",
        "name": "Bitcoin",
        "supply": "19823321.0000000000000000",
        "maxSupply": "21000000.0000000000000000",
        "marketCapUsd": "1939613325892.4607145113457500",
        "volumeUsd24Hr": "12341417371.3505338276601668",
        "priceUsd": "97845.0243474572557500",
        "changePercent24Hr": "1.4324165997531723",
        "vwap24Hr": "96203.8859537212418977",
        "explorer": "https://blockchain.info/"
      },
      "timestamp": 1739399343596
    }

    Recall that you can format USD to four decimal places with a thousands separator with code like:

    print(f"${amount:,.4f}")


"""


import sys
import requests

def main():
  if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
  else:
    try:
      sys.argv[1] = float(sys.argv[1])
    except ValueError:
      sys.exit("Command-line argument is not a number")
  try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a4f145fe9f5a8bf61b32ccfa3be81df15ba3d9750d2b8e0d1338699b99eb5a2b")
    content = response.json()
    price_usd = content["data"]["priceUsd"]
    price_usd = float(price_usd)
    coin_price = price_usd * sys.argv[1]
    print(f"${coin_price:,.4f}")
  except requests.RequestException:
    sys.exit(1)

if __name__ == "__main__":
  main()
