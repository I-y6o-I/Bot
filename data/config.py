from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
NOTIFY_ADMINS = False
ADMINS = env.list("ADMINS")
IP = env.str("ip")

