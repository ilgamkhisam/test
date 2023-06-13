# BOT settings
TOKEN = "6203497113:AAH6qtwCusXhLCR0ZmF4Vrh_jgzCR3TpLHY"
ADMINS_IDS = []


# DATABASE settings
POSTGRES_USER = "ilgam"
POSTGRES_PASSWORD = "qwerty123"
POSTGRES_DATABASE = "eat_time_db"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = 5432

POSTGRES_URL = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}".format(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    name=POSTGRES_DATABASE
)





