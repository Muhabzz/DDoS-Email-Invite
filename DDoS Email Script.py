import requests
import time

# ------------------ Configuration ------------------
url = "https://your-api-endpoint.com/api/graphql"  # Replace with your actual API URL

headers = {
    "Content-Type": "application/json",
    "Cookie": "YOUR_SESSION_TOKEN_HERE",  # Replace with your session token
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Referer": "https://your-website.com",
    "Origin": "https://your-website.com",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
}

# ------------------ Input Data ------------------
email = input("Enter the email address to send or resend an invite to: ").strip()

data = {
    "operationName": "ResendMemberInvite",
    "variables": {
        "email": email
    },
    "query": """
        mutation ResendMemberInvite($email: String!) {
            resendMemberInvite(email: $email)
        }
    """
}

# ------------------ Execution Loop ------------------
repeat_count = 5  # You can change this number

for i in range(repeat_count):
    response = requests.post(url, json=data, headers=headers)
    print(f"[{i+1}] Status Code: {response.status_code}, Response: {response.text}")
    time.sleep(1)  # Add delay to avoid overloading the server
