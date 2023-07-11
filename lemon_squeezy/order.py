import requests
from typing import Dict, Optional

class Order:
    """
    Class for interacting with the 'order' part of the API.
    """

    def __init__(self, session: requests.Session):
        """
        Initialize a new instance of Order.

        Args:
            session (requests.Session): The requests Session to use for making requests.
        """
        self.session = session

    def get_order(self, order_id: int) -> Optional[Dict]:
        """
        Get the details of a specific order.

        Args:
            order_id (int): The ID of the order.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/orders/{order_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error getting order: {e}')
            return None

    def get_all_orders(self, store_id: Optional[int] = None, user_email: Optional[str] = None) -> Optional[Dict]:
        """
        Get the details of all orders, optionally filtered by store ID and user email.

        Args:
            store_id (int, optional): The ID of the store.
            user_email (str, optional): The email of the user.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/orders"
        filters = []
        if store_id:
            filters.append(f'filter[store_id]={store_id}')
        if user_email:
            filters.append(f'filter[user_email]={user_email}')
        if filters:
            url += '?' + '&'.join(filters)

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error getting orders: {e}')
            return None
