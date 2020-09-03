import requests

q = """
{
  movies(offset:10) {
    title
  }
}
"""

resp = requests.post("http://localhost:8000/graphql/", params={'query': q})
print(resp.text)