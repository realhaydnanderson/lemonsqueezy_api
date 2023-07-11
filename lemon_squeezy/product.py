import requests
from typing import Dict, Optional

class Product:
    """
    Class for interacting with the 'product' part of the API.
    """

    def __init__(self, session: requests.Session):
        """
        Initialize a new instance of Product.

        Args:
            session (requests.Session): The requests Session to use for making requests.
        """
        self.session = session

    def get_product(self, product_id: int) -> Optional[Dict]:
        """
        Get the details of a specific product.

        Args:
            product_id (int): The ID of the product.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/products/{product_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error getting product: {e}')
            return None

    def get_all_products(self, store_id: Optional[int] = None) -> Optional[Dict]:
        """
        Get the details of all products, optionally filtered by store ID.

        Args:
            store_id (int, optional): The ID of the store.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/products"
        if store_id:
            url += f'?filter[store_id]={store_id}'

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error getting products: {e}')
            return None
