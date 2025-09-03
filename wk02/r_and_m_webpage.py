import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
</head>
<body>
"""



# Add character cards
for char in data["results"]:
    html_content += f"""
    
    <h2>{char['name']}</h2>
    <img src="{char['image']}" alt="Picture of {char['name']}">       
    <div>
        <ul>
            <li>Species: {char['species']}</li>
            <li>Status: {char['status']}</li>
            <li>Location: {char['location']['name']}</li>
        </ul>
        <a href="{char['url']}">Data Source</a>
    </div>
    """
# End character cards


html_content += """
</body>
</html>
"""
# End HTML structure

# Write to HTML file
with open("rick_and_morty.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_strong.html")

