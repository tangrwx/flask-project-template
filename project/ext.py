from flask_sqlalchemy import SQLAlchemy


class NullSQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super().apply_driver_hacks(app, info, options)

        if info.drivername.startswith("mysql"):
            from sqlalchemy.pool import NullPool

            options["poolclass"] = NullPool

            # Remove pool_size from options to avoid TypeError:
            #   Invalid argument(s) 'pool_size' sent to create_engine()
            options.pop("pool_size", None)
            options.pop("pool_recycle", None)


db = NullSQLAlchemy()
