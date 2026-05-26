import requests
from locust import HttpUser, task, between
from creds import PASSWORD, EMAIL

USER_EMAIL = EMAIL
USER_PASSWORD = PASSWORD
STATIC_REFRESH_TOKEN = "CRxS4UiHZI0xuJubp4s55d95U5VTyGkFHF04D/7YaH8="


class AuthSession:
    def __init__(self, base_url, refresh_token, session):
        self.base_url = base_url
        self.refresh_token = refresh_token
        self.session = session

        self.session.headers.update({
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Content-Type": "application/json",
            "User-Agent":
                "Mozilla/5.0"
                " (Windows NT 10.0; Win64; x64)"
                " AppleWebKit/537.36"
                " (KHTML, like Gecko)"
                " Chrome/148.0.0.0"
                " Safari/537.36"
                " Edg/148.0.0.0",
            "Sec-Ch-Ua": '"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sessionid": "uvo5w400stq",
            "Projectid": "ee43128f-8dce-4816-ab66-0fe87fac1634"
        })

        self.session.hooks['response'].append(self.handle_401)

    def login_by_credentials(self, email, password):
        url = f"{self.base_url}/api/auth/login"
        payload = {"email": email, "password": password}

        response = requests.post(url, json=payload, headers=self.session.headers)
        if response.status_code == 200:
            data = response.json()
            access_token = data.get("authToken")
            if data.get("refreshToken"):
                self.refresh_token = data.get("refreshToken")

            self.session.headers.update({"Authorization": f"Bearer {access_token}"})
            print(f"[Auth] Юзер {email} успешно залогинен.")
            return True
        print(f"[Auth] Ошибка входа для {email}: {response.status_code}")
        return False

    def login_with_refresh(self):
        url = f"{self.base_url}/api/auth/refresh-token"
        payload = {"refreshToken": self.refresh_token}

        refresh_headers = self.session.headers.copy()
        refresh_headers.update({
            "Origin": self.base_url,
            "Referer": f"{self.base_url}/"
        })

        response = requests.post(url, json=payload, headers=refresh_headers)
        if response.status_code == 200:
            data = response.json()
            new_access_token = data.get("authToken")
            self.session.headers.update({"Authorization": f"Bearer {new_access_token}"})
            print("[Auth] Токен успешно обновлен через Refresh!")
            return True
        return False

    def handle_401(self, response, *args, **kwargs):
        if response.status_code == 401 and "refresh-token" not in response.url:
            print(f"[Hook] Поймали 401 на {response.url}. Пробуем обновить токен...")
            if self.login_with_refresh():
                original_request = response.request
                original_request.headers['Authorization'] = self.session.headers['Authorization']
                return self.session.send(original_request, **kwargs)
        return response


class ControlModule(HttpUser):
    host = "https://dev.codiq.io"
    wait_time = between(1, 3)

    def on_start(self):
        self.auth = AuthSession(
            base_url=self.host,
            refresh_token=STATIC_REFRESH_TOKEN,
            session=self.client
        )

        if not self.auth.login_by_credentials(USER_EMAIL, USER_PASSWORD):
            print("[Locust] Прерываем работу юзера, так как авторизация упала.")

    @task
    def get_control_modules(self):
        folder_id = "62fffdc3-0b1e-4a38-54c1-6c635811"

        params = {
            "sortingField": "name",
            "sortDirection": "0",
            "pageSize": "100",
            "page": "1",
            "query": ""
        }

        self.client.get(
            f"/api/elements/by-folder/{folder_id}",
            params=params,
            name="/api/elements/by-folder/[folder_id]"
        )
