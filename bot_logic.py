import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

# Logging setup as per task requirement
logging.basicConfig(
    filename='trading.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BinanceBot:
    def __init__(self, api_key, api_secret):
        # Base URL for Futures Testnet is handled by testnet=True
        self.client = Client(api_key, api_secret, testnet=True)

    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logging.info(f"Attempting {order_type} {side} order for {symbol}")
            
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity
            }

            if order_type.upper() == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders")
                params['price'] = price
                params['timeInForce'] = 'GTC'  # Good Till Cancelled

            # API Request
            response = self.client.futures_create_order(**params)
            logging.info(f"ORDER SUCCESS: {response}")
            return response

        except BinanceAPIException as e:
            logging.error(f"API ERROR: {e.message}")
            return {"status": "error", "message": e.message}
        except Exception as e:
            logging.error(f"SYSTEM ERROR: {str(e)}")
            return {"status": "error", "message": str(e)}