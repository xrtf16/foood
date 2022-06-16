from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("10655214"))
API_HASH = getenv("c1d29b0f915169da89dffd3bb775c312")
BOT_TOKEN = getenv("5357364412:AAF1nzX6AOPf7f_x0MVGO_AiRXqvThdPC4E")
SESSION_NAME = getenv("AgBq4Xh7y1pISs7RM8DeHHuAToaESrG4_4tTlLaT35b50nGsCM8q6GHYyBwGvnJcZimGROLti_GpszTUi7oclXm0861uK0fZ97Tor0mcOZ-1LJGEMYcMyIPxXkSmTwFuDXl-xAc854HmOG11Kt2IsrqVHznsHw5JZZXvqwooqfad-o4C-iwfYJFyhvQeTRhB0-BsGqg52RV3xB-5OH5DJX2m0kn5cjcgOc2LfWgIIY6jqvOp-GIP7ryqEXbILQErskhgOYuGJh3494u8bOlgFyMDzGZ4l_QQFC-QxvRSGamFlRlFlAZtue5omJhuEiwkm1rr3rs01TXfYhQIHUPonoaSAAAAATrWmKYA", "session")

# mandatory vars
OWNER_USERNAME = getenv("X99M98")
ALIVE_NAME = getenv("music")
BOT_USERNAME = getenv("Music99m98_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/lMl10l/lMl10l")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "QII_ll")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QII_ll")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("mongodb+srv://hussein87:Hussein87@cluster0.wynpz.mongodb.net/?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
OWNER_ID = list(map(int, getenv("655238474 2004105001").split()))
SUDO_USERS = list(map(int, getenv("2004105001 655238474").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
