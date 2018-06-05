# fomo-superfilter
Filters the shit out of the shitcoins. Proper.

### EXAMPLE
```python
from fomo_superfilter.interface import BinanceDataFrameCreator
from fomo_superfilter.interface import BittrexDataFrameCreator
from fomo_superfilter.superfilter import SuperFilter

binance_data = BinanceDataFrameCreator.prepare_dataframes()
binance_btc = binance_data['BTC']
binance_filtered = SuperFilter.filter(binance_btc)

print(binance_filtered)

bittrex_data = BittrexDataFrameCreator.prepare_dataframes()
bittrex_btc = bittrex_data['BTC']
bittrex_filtered = SuperFilter.filter(bittrex_btc)

print(bittrex_filtered)
```
