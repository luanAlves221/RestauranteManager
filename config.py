DATABASE_HOST = "localhost"
DATABASE_USER = "root"
DATABASE_PASSWORD = ""
DATABASE_NAME = "RestauranteManager"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
)

SECRET_KEY = "chave_secreta"
