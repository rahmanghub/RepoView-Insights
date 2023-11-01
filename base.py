import requests
import matplotlib.pyplot as plt

username = "----username------"
token = "------------pac--------------"

base_url = f"https://api.github.com/users/{username}/repos"
query = "is:public"

headers = {
    "Authorization": f"token {token}"
}
params = {
    "q": query,
    "per_page": 100 
}

def get_repository_views(repo_owner, repo_name):
    endpoint = f"https://api.github.com/repos/{repo_owner}/{repo_name}/traffic/views"
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.get(endpoint, headers=headers)
    data = response.json()

    if response.status_code == 200:
        return data["count"]
    else:
        print(f"Error getting views for {repo_owner}/{repo_name}: {response.status_code}")
        return None

repository_names = []
view_counts = []

response = requests.get(base_url, headers=headers, params=params)
response.raise_for_status()
data = response.json()

for repo in data:
    print([repo["owner"]["login"], repo["name"]])
    views = get_repository_views(repo["owner"]["login"], repo["name"])
    if views is not None:
        repository_names.append(f"{repo['owner']['login']}/{repo['name']}")
        view_counts.append(views)

print(repository_names)
print(view_counts)


plt.figure(figsize=(10, 6))
plt.barh(repository_names, view_counts, color='skyblue')
plt.xlabel('Views')
plt.title('GitHub Public Repository Views')
plt.gca().invert_yaxis()
plt.show()
