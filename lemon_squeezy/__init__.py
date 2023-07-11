import requests
from typing import Dict
from .variants import Variants
from .checkout import Checkout
from .subscription import Subscription
from .customer import Customer
from .product import Product
from .order import Order

class LemonSqueezy:
    """
    Main class for interacting with the API.
    """
    
    def __init__(self, api_url: str, api_key: str):
        """
        Initialize a new instance of LemonSqueezy.

        Args:
            api_url (str): The URL of the API.
            api_key (str): The API key for authentication.
        """
        self.session = self._create_session(api_url, api_key)

        # Pass the session instead of individual config parameters
        self.variants = Variants(self.session)
        self.checkout = Checkout(self.session)
        self.subscription = Subscription(self.session)
        self.customer = Customer(self.session)
        self.product = Product(self.session)
        self.order = Order(self.session)

    def _create_session(self, api_url: str, api_key: str) -> requests.Session:
        """
        Create a new requests Session with the necessary headers and configs.

        Args:
            api_url (str): The URL of the API.
            api_key (str): The API key for authentication.

        Returns:
            requests.Session: The created Session object.
        """
        session = requests.Session()
        session.headers.update({
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {api_key}'
        })
        session.params.update({
            'api_url': api_url,
        })

        return session
