import requests
from typing import Dict, Optional

class Variants:
    """
    Class for interacting with the 'variants' part of the API.
    """

    def __init__(self, session: requests.Session):
        """
        Initialize a new instance of Variants.

        Args:
            session (requests.Session): The requests Session to use for making requests.
        """
        self.session = session

    def get_variant(self, variant_id: int) -> Optional[Dict]:
        """
        Get the details of a specific variant.

        Args:
            variant_id (int): The ID of the variant.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/variants/{variant_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error getting variant: {e}')
            return None

    def get_all_variants(self, product_id: Optional[int] = None) -> Optional[Dict]:
        """
        Get the details of all variants, optionally filtered by product ID.

        Args:
            product_id (int, optional): The ID of the product.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/variants"
        if product_id:
            url += f'?filter[product_id]={product_id}'

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error getting variants: {e}')
            return None
