AUTHOR = "BPV"
SITENAME = "LightEcho Blog"
SITEURL = ""
LOGO_URL = "images/lightecho-icon-300x300.png"

THUMBNAIL_DIR = "images/thumbnails"

PATH = "content"
THEME = "notmyidea"

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
    "images/lightecho-icon.ico",
    "static",
]
EXTRA_PATH_METADATA = {"images/lightecho-icon.ico": {"path": "favicon.ico"}}

TOP_LINKS = (
    ("BPV", "https://bpventures.us/"),
    ("Lightecho.io", "https://lightecho.io/"),
)

LINKS = (
    ("GitHub", "https://github.com/bp-ventures/lightecho-stellar-oracle"),
    (
        "Stellar",
        "https://stellar.expert/explorer/public/contract/CDOR3QD27WAAF4TK4MO33TGQXR6RPNANNVLOY277W2XVV6ZVJ6X6X42T",
    ),
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/LightechoI"),
    ("Youtube", "https://www.youtube.com/@lightecho5266"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
