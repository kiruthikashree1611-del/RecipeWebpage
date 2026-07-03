from IPython.display import HTML

HTML("""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Recipe Webpage</title>

<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f8f8f8;
    margin: 0;
    padding: 0;
}

header {
    background-color: #ff6b6b;
    color: white;
    text-align: center;
    padding: 20px;
}

.container {
    width: 80%;
    margin: auto;
    background: white;
    padding: 20px;
    margin-top: 20px;
    border-radius: 10px;
}

img {
    width: 100%;
    max-width: 500px;
    display: block;
    margin: auto;
    border-radius: 10px;
}

h2 {
    color: #ff6b6b;
}

ul, ol {
    line-height: 1.8;
}

@media (max-width: 768px) {
    .container {
        width: 95%;
    }
}
</style>
</head>

<body>

<header>
    <h1>🍽️ Masala Dosa Recipe</h1>
</header>

<div class="container">

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5b/Masala_Dosa.jpg" alt="Masala Dosa">

<section>
<h2>Ingredients</h2>
<ul>
<li>2 cups dosa batter</li>
<li>2 boiled potatoes</li>
<li>1 chopped onion</li>
<li>1 tsp mustard seeds</li>
<li>Salt to taste</li>
<li>Oil as needed</li>
</ul>
</section>

<section>
<h2>Preparation Steps</h2>
<ol>
<li>Heat oil and add mustard seeds.</li>
<li>Add chopped onions and sauté until golden brown.</li>
<li>Add mashed potatoes and salt, then mix well.</li>
<li>Spread dosa batter on a hot pan.</li>
<li>Place the potato filling in the center.</li>
<li>Fold the dosa and serve hot.</li>
</ol>
</section>

</div>

</body>
</html>
""")
