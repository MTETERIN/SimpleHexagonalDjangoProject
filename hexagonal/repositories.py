from hexagonal.exceptions import EntityDoesNotExist
from hexagonal.models import ORMProduct
from hexagonal.entities import Product


class ProductDatabaseRepo(object):

    def get_product(self, reference):
        try:
            orm_product = ORMProduct.objects \
                                       .get(reference=reference)
        except ORMProduct.DoesNotExist:
            raise EntityDoesNotExist()

        return self._decode_orm_product(orm_product)

    def _decode_orm_product(self, orm_product):
        return Product(reference=orm_product.reference,
                       brand_id=orm_product.brand_id)

class ProductRepo(object):

    def __init__(self, db_repo):
        self.db_repo = db_repo

    def get_product(self, reference):
        # U can add here cache
        product = self.db_repo.get_product(reference)
        return product