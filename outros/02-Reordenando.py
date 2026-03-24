import pandas as pd;

arquivo = pd.read_csv("outros/datasets/world_imdb_movies_top_movies_per_year.csv");
d1 = pd.DataFrame(arquivo);
d1 = d1[["year", "genre", "title"]]

print(
    "Filmes ordenados por ano e gênero:\n",
    d1.sort_values(by=["year","genre"])
)