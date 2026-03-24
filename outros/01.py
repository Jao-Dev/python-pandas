import pandas as pd;

arquivo = pd.read_csv("outros/datasets/br_ibge_censo_2022_alfabetizacao_grupo_idade_sexo_raca.csv");
d1 = pd.DataFrame(arquivo);

filtro1 = d1["grupo_idade"].loc[d1["grupo_idade"] == "15 a 19 anos"];


print("Grupos separados por idades:\n",d1["grupo_idade"].unique());
print("\nNúmero de alfabetizados no grupo de 15 a 19 anos: ",filtro1.count());

