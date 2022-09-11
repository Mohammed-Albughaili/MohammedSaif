import matplotlib.pyplot as plt
import numpy as np
import random
Gammas = []
Dists = []
for x in range(100000):
    Gammas.append(random.gauss(10,20))
    Dists.append(random.gauss(3.7, 1))
Dir2 = "MPI"

plt.figure(figsize=[15, 8])
plt.plot(Dists, Gammas, "k.")
plt.yticks([0, 10, 20, 30, 40, 50, 60], fontsize=20)
plt.ylim([0, 30])
plt.xticks([0.2, 0.5, 1.0, 1.4, 1.8, 2.6, 3.0, 3.5, 4.0], fontsize=25, rotation=90)
plt.ylim([0.2, 4])
plt.grid()
plt.ylabel(r"Mutations-types", fontsize=25)
plt.xlabel("Genes", fontsize=25)
plt.title((r"Mutations+types" + Dir2), y=1.5, fontsize=25)
plt.tight_layout()
plt.show()
plt.savefig(("Distance_Gamma_" + Dir2 + ".png"))
plt.close()


values =[]
values2 =[]
values3 =[]
for x in range(30):
    values.append(random.randint(1, 5) * random.random())
    values2.append(random.randint(1, 5) * random.random())
    values3.append(random.randint(1, 5) * random.random())
plt.figure(figsize=[15, 8])
plt.bar(list(range(30)), values)
plt.title("Cutis Laxa", fontsize=25)
plt.xlabel("GORAB", fontsize=25, rotation=90)
plt.ylabel("ALDH18", fontsize=25)
plt.xlim([0, 30])
plt.ylim([0, 8])
plt.yticks(list(range(10)), fontsize=25)
plt.yticks(list(range(15)), fontsize=25)
plt.grid(axis="y")
plt.tight_layout()
plt.show()
plt.savefig(("Cutis Laxa_Example.png"))
plt.close()



values.sort()
values2.sort()
values3.sort()

plt.figure(figsize=[10, 20])
plt.plot(list(range(30)), values)
plt.plot(list(range(30)), values2, "r.", markersize=15)
plt.plot(list(range(30)), values3, "*g ", markersize=15)
plt.title("Cutis Laxa", fontsize=25)
plt.xlabel("GORAB", fontsize=25, rotation=90)
plt.ylabel("ALDH18", fontsize=25)
plt.xlim([-1, 10])
plt.ylim([0, 8])
plt.yticks(list(range(9)), fontsize=25)
plt.xticks(list(range(20)), fontsize=25, rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig(("Cutis Laxa_Example.png"))
plt.close()

x = np.array([10, 15, 20, 30, 35, 40, 45, 50, 60])
y = np.array([100, 110, 120, 130, 140, 150,160])

plt.plot(x, y)
plt.title("Tumer")
plt.xlabel("Benign tumer")
plot.ylabel("Malignant tumer")
