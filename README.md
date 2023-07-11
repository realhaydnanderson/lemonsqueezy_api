#🍋 Lemon Squeezy API Wrapper
Python Integration of the Lemon Squeezy API wrapper.

##🧩 Modules
Here's a brief overview of the modules in Lemon Squeezy:

customer.py: Module for customer-related operations.
variants.py: Module for handling product variants.
product.py: Module for managing products.
checkout.py: Module for checkout operations.
order.py: Module for order management.
subscription.py: Module for managing subscriptions.

##🛠 Usage
Here's a simple example to get you started:

python
Copy code
from lemon_squeezy import LemonSqueezy

ls = LemonSqueezy("https://api.lemonsqueezy.com", <API_KEY>)
products = ls.product.get_all_products()
Remember to replace <API_KEY> with your actual API key.

##👥 Contribution
We love contributions! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request!
