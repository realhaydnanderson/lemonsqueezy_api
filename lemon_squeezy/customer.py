from typing import Dict, Optional
import requests

class Customer:
    """
    Class for interacting with the customer part of the API.
    """

    def __init__(self, session: requests.Session):
        """
        Initialize a new instance of Customer.

        Args:
            session (requests.Session): The requests Session to use for making requests.
        """
        self.session = session

    def get_customer(self, customer_id: str) -> Optional[Dict]:
        """
        Get information about a single customer.

        Args:
            customer_id (str): The ID of the customer.

        Returns:
            Dict: The JSON response from the API, or None if the request failed.
        """
        url = f"{self.session.params['api_url']}/v1/customers/{customer_id}"

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error getting customer: {e}")
            return None

    def get_all_customers(self, store_id: str = None, email: str = None) -> Optional[Dict]:
        """
        Get information about all customers, with optional filters.

        Args:
            store_id (str, optional): If provided, only return customers from this store.
            email (str, optional): If provided, only return customers with this email.

        Returns:
            Dict: The JSON response from the API, or None if the request failed.
        """
        url = f"{self.session.params['api_url']}/v1/customers"
        filters = []
        if store_id:
            filters.append(f"filter[store_id]={store_id}")
        if email:
            filters.append(f"filter[email]={email}")
        if filters:
            url += "?" + "&".join(filters)

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Error getting customers: {e}")
            return None
