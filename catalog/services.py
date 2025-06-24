from catalog.models import Product


class ProductService:
    @staticmethod
    def get_list_product_in_category(category_id):
        return Product.objects.filter(category_id=category_id)
