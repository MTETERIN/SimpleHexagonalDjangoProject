from hexagonal.repositories import ProductDatabaseRepo, ProductRepo
from hexagonal.interactors import GetProductInteractor
from hexagonal.views import ProductView


class ProductDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return ProductDatabaseRepo()


class ProductRepoFactory(object):

    @staticmethod
    def get():
        db_repo = ProductDatabaseRepoFactory.get()
        return ProductRepo(db_repo)


class GetProductInteractorFactory(object):

    @staticmethod
    def get():
        product_repo = ProductRepoFactory.get()
        return GetProductInteractor(product_repo)


class ProductViewFactory(object):

    @staticmethod
    def create():
        get_product_interactor = GetProductInteractorFactory.get()
        return ProductView(get_product_interactor)