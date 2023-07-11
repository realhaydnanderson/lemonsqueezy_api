import requests
from typing import Dict, Optional

class Checkout:
    """
    Class for interacting with the 'checkout' part of the API.
    """

    def __init__(self, session: requests.Session):
        """
        Initialize a new instance of Checkout.

        Args:
            session (requests.Session): The requests Session to use for making requests.
        """
        self.session = session

    def build_product_options(self, name=None, description=None, media=None, redirect_url=None, receipt_button_text=None, receipt_link_url=None, receipt_thank_you_note=None, enabled_variants=None):
        product_options = {}
        if name: 
            product_options['name'] = name
        if description:
            product_options['description'] = description
        if media:
            product_options['media'] = media
        if redirect_url:
            product_options['redirect_url'] = redirect_url
        if receipt_button_text:
            product_options['receipt_button_text'] = receipt_button_text
        if receipt_link_url:
            product_options['receipt_link_url'] = receipt_link_url
        if receipt_thank_you_note:
            product_options['receipt_thank_you_note'] = receipt_thank_you_note
        if enabled_variants:
            product_options['enabled_variants'] = enabled_variants
        return product_options

    def build_checkout_options(self, embed=None, media=None, logo=None, desc=None, discount=None, dark=None, subscription_preview=None, button_color=None):
        checkout_options = {}
        if embed is not None:
            checkout_options['embed'] = embed
        if media is not None:
            checkout_options['media'] = media
        if logo is not None:
            checkout_options['logo'] = logo
        if desc is not None:
            checkout_options['desc'] = desc
        if discount is not None:
            checkout_options['discount'] = discount
        if dark is not None:
            checkout_options['dark'] = dark
        if subscription_preview is not None:
            checkout_options['subscription_preview'] = subscription_preview
        if button_color:
            checkout_options['button_color'] = button_color
        return checkout_options




    def build_checkout_data(self, email: Optional[str] = None, name: Optional[str] = None, 
                            billing_address_country: Optional[str] = None, billing_address_zip: Optional[str] = None,
                            tax_number: Optional[str] = None, discount_code: Optional[str] = None, 
                            custom: Optional[Dict] = None) -> Dict:
        """
        Build the checkout data dictionary.

        Args:
            email (str, optional): The email of the customer.
            name (str, optional): The name of the customer.
            billing_address_country (str, optional): The country of the billing address.
            billing_address_zip (str, optional): The zip code of the billing address.
            tax_number (str, optional): The tax number.
            discount_code (str, optional): The discount code.
            custom (Dict, optional): Any custom data.

        Returns:
            Dict: The built checkout data.
        """
        checkout_data = {}
        if email:
            checkout_data['email'] = email
        if name:
            checkout_data['name'] = name
        if billing_address_country:
            checkout_data['billing_address.country'] = billing_address_country
        if billing_address_zip:
            checkout_data['billing_address.zip'] = billing_address_zip
        if tax_number:
            checkout_data['tax_number'] = tax_number
        if discount_code:
            checkout_data['discount_code'] = discount_code
        if custom:
            checkout_data['custom'] = custom
        return checkout_data

    def create_checkout(self, store_id: int, variant_id: int, custom_price: Optional[float] = None, 
                        product_options: Optional[Dict] = None, checkout_options: Optional[Dict] = None,
                        checkout_data: Optional[Dict] = None, preview: Optional[bool] = None, 
                        expires_at: Optional[str] = None) -> Optional[Dict]:
        """
        Create a new checkout.

        Args:
            store_id (int): The ID of the store.
            variant_id (int): The ID of the variant.
            custom_price (float, optional): The custom price.
            product_options (Dict, optional): The product options.
            checkout_options (Dict, optional): The checkout options.
            checkout_data (Dict, optional): The checkout data.
            preview (bool, optional): Whether this is a preview.
            expires_at (str, optional): When the checkout expires.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/checkouts"
        payload = {
            'data': {
                'type': 'checkouts',
                'relationships': {
                    'store': {
                        'data': {
                            'type': 'stores',
                            'id': store_id
                        }
                    },
                    'variant': {
                        'data': {
                            'type': 'variants',
                            'id': variant_id
                        }
                    }
                }
            }
        }

        if custom_price or product_options or checkout_options or checkout_data or preview is not None or expires_at:
            payload['data']['attributes'] = {}
            if custom_price:
                payload['data']['attributes']['custom_price'] = custom_price
            if product_options:
                payload['data']['attributes']['product_options'] = product_options
            if checkout_options:
                payload['data']['attributes']['checkout_options'] = checkout_options
            if checkout_data:
                payload['data']['attributes']['checkout_data'] = checkout_data
            if preview is not None:
                payload['data']['attributes']['preview'] = preview
            if expires_at:
                payload['data']['attributes']['expires_at'] = expires_at

        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error creating checkout: {e}')
            return None

    def list_checkouts(self, store_id: Optional[int] = None, variant_id: Optional[int] = None) -> Optional[Dict]:
        """
        List all checkouts, optionally filtered by store ID and variant ID.

        Args:
            store_id (int, optional): The ID of the store.
            variant_id (int, optional): The ID of the variant.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/checkouts"
        params = {}
        if store_id is not None:
            params['filter[store_id]'] = store_id
        if variant_id is not None:
            params['filter[variant_id]'] = variant_id

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error listing checkouts: {e}')
            return None

    def retrieve_checkout(self, checkout_id: int) -> Optional[Dict]:
        """
        Retrieve a specific checkout.

        Args:
            checkout_id (int): The ID of the checkout.

        Returns:
            Dict: The JSON response from the API.
        """
        url = f"{self.session.params['api_url']}/v1/checkouts/{checkout_id}"

        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Error retrieving checkout: {e}')
            return None
