import pandas as pd

df = pd.read_csv("./nouns.csv", sep="\t", usecols=["bare"])

df.columns = ["word"]

print(df.head())

words_list = df["word"].tolist()
print(f"Список слов (первые 5): {words_list[:5]}")

df.to_csv("./words.csv", index=False, header=False)

with open("./words_list.txt", "w") as f:
    f.write("\n".join(words_list))
