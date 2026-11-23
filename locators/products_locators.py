
PHONES_CATEGORY = "Phones & PDAs"
TABLETS_CATEGORY = "Tablets (1)"
ADD_TO_CART_SUCCESS_MESSAGE = "//div[contains(@class, 'alert-success')]"


def add_to_cart_button(product_name: str) -> str:
    return (
        f"//a[contains(text(), '{product_name}')]"
        "/ancestor::div[contains(@class, 'product-thumb')]"
        "//div[@class='button-group']"
        "/button[.//span[contains(text(), 'Add to Cart')]]"
    )
