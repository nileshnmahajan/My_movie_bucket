import requests

q = """
{
  movie(id:737329) {
    title
  }
}
"""

resp = requests.post("http://localhost:8000/graphql/", params={'query': q})
print(resp.text)