class Locators:
    heading_text_element= '//android.widget.TextView[@text="PRODUCTS"]'
    remove_button_element= '//android.widget.TextView[@text="REMOVE"]'
    cart_badge_element= '//android.view.ViewGroup[@content-desc="test-Cart"]/descendant::android.widget.TextView'
    add_button_element= './/android.view.ViewGroup[@content-desc="test-ADD TO CART"]'

    @staticmethod
    def product_element(product_name):
        return f'//android.widget.TextView[@text="{product_name}"]/..'