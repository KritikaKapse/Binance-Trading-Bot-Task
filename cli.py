import click
from bot_logic import BinanceBot

# Replace with your actual Testnet API Keys
API_KEY = 'YOUR_TESTNET_API_KEY'
API_SECRET = 'YOUR_TESTNET_API_SECRET'

@click.command()
@click.option('--symbol', prompt='Symbol (e.g., BTCUSDT)', help='The trading pair.')
@click.option('--side', type=click.Choice(['BUY', 'SELL'], case_sensitive=False), prompt='Side', help='BUY or SELL.')
@click.option('--type', 'order_type', type=click.Choice(['MARKET', 'LIMIT'], case_sensitive=False), prompt='Order Type', help='MARKET or LIMIT.')
@click.option('--quantity', type=float, prompt='Quantity', help='Amount to trade.')
@click.option('--price', type=float, required=False, help='Price for LIMIT orders.')
def main(symbol, side, order_type, quantity, price):
    bot = BinanceBot(API_KEY, API_SECRET)
    
    click.echo(f"\n--- Order Summary ---")
    click.echo(f"Symbol: {symbol} | Side: {side} | Type: {order_type} | Qty: {quantity}")
    
    result = bot.place_futures_order(symbol, side, order_type, quantity, price)
    
    if result.get('status') == 'error':
        click.secho(f"Failure: {result.get('message')}", fg='red')
    else:
        click.secho(f"Success! Order ID: {result.get('orderId')}", fg='green')
        click.echo(f"Status: {result.get('status')} | Avg Price: {result.get('avgPrice', 'N/A')}")

if __name__ == '__main__':
    main()