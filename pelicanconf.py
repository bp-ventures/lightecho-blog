AUTHOR = "BPV"
SITENAME = "LightEcho Blog"
SITEURL = ""
# LOGO_URL = "images/lightMode-lightecho-logo.dd70c7a3.svg"

PATH = "content"

TIMEZONE = "Europe/Rome"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


STATIC_PATHS = [
    "images",
    "images/favicon.ico",
    "static",
]
EXTRA_PATH_METADATA = {"images/favicon.ico": {"path": "favicon.ico"}}

# TEMPLATE_CONTEXTS = {
#     "logo_url": LOGO_URL,
# }

# Blogroll
LINKS = (
    ("Lightecho FAQ", "https://lightecho.io/faq"),
    ("BPV", "https://bpventures.us/"),
    ("Lightecho.io", "https://lightecho.io/"),
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/LightechoI"),
    ("Youtube", "https://www.youtube.com/@lightecho5266"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
