import requests
from typing import Dict, Optional

class Subscription:
    """
    Class for interacting with the 'subscription' part of the API.
    """

    def __init__(self, session: requests.Session):
        """
        Initialize a new instance of Subscription.

        Args:
            session (requests.Session): The requests Session to use for making requests.
        """
        self.session = session

    def get_subscription(self, subscription_id: int) -> Optional[Dict]:
        """
        Get the details of a specific subscription.

        Args:
            subscription_id (int): The ID of the subscription.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/subscriptions/{subscription_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error getting subscription: {e}')
            return None

    def update_subscription(self, subscription_id: int, data: Dict) -> Optional[Dict]:
        """
        Update a specific subscription.

        Args:
            subscription_id (int): The ID of the subscription.
            data (Dict): The data to update.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/subscriptions/{subscription_id}"
        try:
            response = self.session.patch(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error updating subscription: {e}')
            return None

    def delete_subscription(self, subscription_id: int) -> Optional[Dict]:
        """
        Delete a specific subscription.

        Args:
            subscription_id (int): The ID of the subscription.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/subscriptions/{subscription_id}"
        try:
            response = self.session.delete(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error deleting subscription: {e}')
            return None

    def list_subscriptions(self, store_id: Optional[int] = None, order_id: Optional[int] = None, 
                           order_item_id: Optional[int] = None, product_id: Optional[int] = None, 
                           variant_id: Optional[int] = None) -> Optional[Dict]:
        """
        List all subscriptions, optionally filtered by store ID, order ID, order item ID, product ID, and variant ID.

        Args:
            store_id (int, optional): The ID of the store.
            order_id (int, optional): The ID of the order.
            order_item_id (int, optional): The ID of the order item.
            product_id (int, optional): The ID of the product.
            variant_id (int, optional): The ID of the variant.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/subscriptions"
        params = {}
        if store_id is not None:
            params['filter[store_id]'] = store_id
        if order_id is not None:
            params['filter[order_id]'] = order_id
        if order_item_id is not None:
            params['filter[item_id]'] = order_item_id
        if product_id is not None:
            params['filter[product_id]'] = product_id
        if variant_id is not None:
            params['filter[variant_id]'] = variant_id

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error listing subscriptions: {e}')
            return None
