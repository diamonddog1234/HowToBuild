from core.auth.urls import urls as auth_urls
from houses.urls import urls as houses_urls
from tubes.urls import urls as samples_url

urls = [
    *auth_urls,
    *houses_urls,
    *samples_url
]




