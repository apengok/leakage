
class DmaRouter:
    """
    A router to control all database operations on models in the
    dma application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read dma models go to dma_db.
        """
        if model._meta.app_label == 'dma':
            return 'dma_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write dma models go to dma_db.
        """
        if model._meta.app_label == 'dma':
            return 'dma_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the dma app is involved.
        """
        if obj1._meta.app_label == 'dma' or \
           obj2._meta.app_label == 'dma':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the dma app only appears in the 'dma_db'
        database.
        """
        if app_label == 'dma':
            return db == 'dma_db'
        return None