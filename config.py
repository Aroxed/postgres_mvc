import os
DB_LABEL = 'db42'
DATABASE = {
        "NAME": os.environ.get("DB_%s_NAME" % DB_LABEL),
        "USER": os.environ.get("DB_%s_USERNAME" % DB_LABEL),
        "PASSWORD": os.environ.get("DB_%s_PASSWORD" % DB_LABEL),
        "HOST": os.environ.get("DB_%s_HOST" % DB_LABEL),
        "PORT": os.environ.get("DB_%s_PORT" % DB_LABEL)
}
