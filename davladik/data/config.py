from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN") #'6050554927:AAGm86nqRNJIQlJSP24I4K-B9itoRrzYSDg'
ADMINS = env.list("ADMINS")
IP = env.str("ip")
Maier = 1140069329
