from abc import ABC, abstractmethod
from typing import List, Dict

class SignalAdapter(ABC):

    @abstractmethod
    def fetch_signals(self) -> List[Dict]:
        """
        Return a list of raw intent signals.
        Each signal must minimally include:
        - topic
        - confidence
        - authenticity
        """
        pass
