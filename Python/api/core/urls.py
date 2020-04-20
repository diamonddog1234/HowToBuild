from core.auth.urls import urls as auth_urls
from houses.urls import urls as houses_urls

urls = [
    *auth_urls,
    *houses_urls
]




