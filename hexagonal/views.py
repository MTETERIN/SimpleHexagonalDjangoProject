from hexagonal.serializers import ProductSerializer
from hexagonal.exceptions import EntityDoesNotExist


class ProductView(object):

    def __init__(self, get_product_interactor):
        self.get_product_interactor = get_product_interactor

    def get(self, reference):
        try:
            product = self.get_product_interactor \
                              .set_params(reference=reference) \
                              .execute()
        except EntityDoesNotExist:
            body = {'error': 'Product does not exist!'}
            status = 404
        else:
            body = ProductSerializer.serialize(product)
            status = 200

        return body, status