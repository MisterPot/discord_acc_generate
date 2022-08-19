import requests
from .rand_data import BIRTH_DATE, PASSWORD
from twocaptcha import TwoCaptcha


def register_new_account(email: str, username: str) -> dict:
    session = requests.Session()
    payload = {
        "captcha_key": None,
        "consent": True,
        "date_of_birth": BIRTH_DATE(),
        "email": email,
        "gift_code_sku_id": None,
        "invite": None,
        "password": PASSWORD(),
        "username": username,
    }

    session.headers.update({
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3235.0 "
                      "Safari/537.36",
        "referer": "https://www.google.com/"
    })

    fingerprint = session.post('https://discord.com/api/v6/auth/fingerprint').json()['fingerprint']
    first_post = session.post('https://discord.com/api/v9/auth/register', json=payload)
    data = first_post.json()

    if data.get('captcha_sitekey') is None:
        raise KeyError("Email already in use or email is invalid")

    code = TwoCaptcha('097ccc9e4a1debbb268b0291bf1f8590') \
        .hcaptcha(
            sitekey=data['captcha_sitekey'],
            url=first_post.url
        )['code']

    return session.post('https://discord.com/api/v9/auth/register', json={
        **payload,
        "captcha_key": code,
        "fingerprint": fingerprint
    }, headers={"X-Fingerprint": fingerprint, "X-Super-Properties": ""}).json()
