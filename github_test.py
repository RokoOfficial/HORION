import os
import json
import urllib.request

API_BASE = 'https://api.github.com'


def github_api_get(endpoint: str):
    token = os.getenv('GITHUB_TOKEN')
    url = f"{API_BASE}{endpoint}"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'HORION-test-script')
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def main():
    username = os.getenv('USUARIO_GITHUB')
    endpoint = f"/users/{username}" if username else '/user'
    data = github_api_get(endpoint)
    print(f"Login: {data.get('login')}")
    print(f"Public repos: {data.get('public_repos')}")


if __name__ == '__main__':
    main()
