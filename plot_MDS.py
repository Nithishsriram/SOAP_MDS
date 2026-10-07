import matplotlib.pyplot as plt

labels = [
    "S1", "S2", "S3", "S4", "S5",
    "S6", "S7", "S8", "S9", "S10",
    "S11", "S12", "S13", "S14", "S15",
    "S16", "S17", "S18", "S19", "S20"
]

plt.figure(figsize=(7, 6))

plt.scatter(embedding[:, 0], embedding[:,1])

for i, label in enumerate(labels):
  plt.text(
      embedding[i, 0],
      embedding[i, 1],
      label,
      fontsize=12
  )

plt.xlabel("e1")
plt.ylabel("e2")
plt.title("MDS")

plt.tight_layout()
plt.show()