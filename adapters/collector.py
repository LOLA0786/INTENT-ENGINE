from typing import List
from adapters.base import SignalAdapter

def collect_signals(adapters: List[SignalAdapter]):
    signals = []
    for adapter in adapters:
        signals.extend(adapter.fetch_signals())
    return signals
