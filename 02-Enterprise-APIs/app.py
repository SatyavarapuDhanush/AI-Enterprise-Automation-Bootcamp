from src import employeeService
from src import api_client


client = api_client.APIClient("https://jsonplaceholder.typicode.com")

users_data=client.get("users")

print("Users Data:")
count = 0
for user in users_data:
    count += 1
    print(f"{count}. {user['name']} - {user['email']}")
    if count >= 10:
        break

# posts_data=client.get("posts")


# print("Posts Data:")
# count = 0
# for post in posts_data:
#     count += 1
#     print(f"{count}. {post['title']} - {post['body']}")
#     if count >= 10:
#         break

employee_service = employeeService.EmployeeService(client)
users =  employee_service.get_all_users()
print(f"Retrieved {len(users)} users. First user: {users[0]['name']}")

payload = {
    "title": "Enterprise Automation",
    "body": "Learning REST APIs",
    "userId": 1
}

created_post = client.post("posts", data=payload)
print("Post created successfully.")
print(created_post)