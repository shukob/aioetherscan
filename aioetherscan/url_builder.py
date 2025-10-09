from urllib.parse import urljoin


class UrlBuilder:
    API_URL = 'https://api.etherscan.io/v2/api'
    BASE_URL = 'https://etherscan.io'

    def __init__(self, api_key: str, chain_id: int = 1) -> None:
        self._API_KEY = api_key
        self._chain_id = chain_id

    @property
    def currency(self) -> str:
        return 'ETH'

    def get_link(self, path: str) -> str:
        return urljoin(self.BASE_URL, path)

    def filter_and_sign(self, params: dict):
        return self._sign(self._filter_params(params or {}))

    def _sign(self, params: dict) -> dict:
        if not params:
            params = {}
        params['apikey'] = self._API_KEY
        params['chainid'] = self._chain_id
        return params

    @staticmethod
    def _filter_params(params: dict) -> dict:
        return {k: v for k, v in params.items() if v is not None}
