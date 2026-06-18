import requests
from typing import Optional, Dict


class SimpleAPIClient:

    def __init__(self, base_url: str = 'https://jsonplaceholder.typicode.com'):
        self.posts_url = f"{base_url}/posts"
        print(f"Client initialized for POSTS at: {self.posts_url}")

    def fetch_post(self, post_id: int) -> Optional[Dict]:
        url = f"{self.posts_url}/{post_id}"
        print(f"\n--- Fetching Post ID: {post_id} ---")

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Success (Status 200).")
                return response.json()
            else:
                print(f"Failed to fetch. Status code: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during GET request: {e}")
            return None

    def create_post(self, title: str, body: str, user_id: int) -> Optional[Dict]:

        print("\n--- Creating New Post ---")
        new_post_data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        try:
            response = requests.post(self.posts_url, json=new_post_data)
            if response.status_code == 201:
                print("Post created successfully (Status 201).")
                return response.json()
            else:
                print(f"Failed to create post. Status code: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during POST request: {e}")
            return None

client = SimpleAPIClient()

post_10 = client.fetch_post(post_id=10)

if post_10:
    print(f"Post Title: {post_10['title']}")

created_item = client.create_post(
    title="Simple Class Demo",
    body="Testing the simple API client's POST functionality.",
    user_id=42
)

if created_item:
    print(f"Created Item ID: {created_item['id']}")
    print(f"Title sent: {created_item['title']}")
