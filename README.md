<div align="center">

# Local Search

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-6.3-blue?logo=plotly&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10-11557c?logo=python&logoColor=white)

</div>

## 📘 Deskripsi

Di sini, kami membuat package `Python` untuk mengimplementasikan algoritma **local search** termasuk _hill climbing_, _simulated annealing_, dan _genetic algorithm_ untuk menyelesaikan masalah penempatan paket-paket dalam truk. Diimplementasikan representasi lingkungan yang meliputi paket, truk, _state_, batasan, aksi, dan fungsi objektif dengan pendekatan _object-oriented programming_ dan visual. Lalu, diimplementasikan algoritma _hill climbing_, _simulated annealing_, dan _genetic algorithm_ mengikuti [Russel and Norvig (2021)](https://aima.cs.berkeley.edu/). Akhirnya, dilakukan analisis hasil dan perbandingan algoritma dalam menyelesaikan persoalan tersebut. Pembahasan selengkapnya dapat dilihat di [laporan](docs/IF3170_G60_MoreArtificialThanIntelligence.pdf).

---

## ✨ Fitur Utama

- 🥇 **Representasi Persoalan**
   - Implementasi representasi paket, truk, dan interaksi mereka dalam suatu _state_ berbasis objek.
   - Implementasi fungsi-fungsi aksi dan objektif agar algoritma _local search_ bisa menyelesaikan dengan persoalan.
- 🥈 **Algoritma Local Search**
   - _Hill Climbing_: diimplementasikan varian _steepest ascent_, _sideways move_, _stochastic_, dan _random restart_.
   - _Simulated Annealing_: diimplementasikan beragam _schedule_ temperatur (geometrik, linear, rasional, dan logaritmik).
   - _Genetic Algorithm_: diimplementasikan mekanisme _selection_, _crossover_, dan _mutation_ yang sesuai.
- 🥉 **Visualisasi**
   - Visualisasi 3D keadaan lingkungan yang interaktif.
   - Menggunakan package `Plotly`.

---

## 📁 Struktur Folder

```
IF3170_G60_MoreArtificialThanIntelligence/
├── doc/
│   └── laporan.pdf
├── output/
│   ├── hill_climbing.py
│   ├── simulated_annealing.py
│   ├── genetic_algorithm.py
│   └── comparison.py
├── src/
│   ├─ engine/
│   │  ├── package.py
│   │  ├── truck.py
│   │  ├── state.py
│   │  ├── constraints.py
│   │  ├── moves.py
│   │  └── objectives.py
│   ├─ solvers/
│   │  ├── hill_climbing.py
│   │  ├── simulated_annealing.py
│   │  └── genetic_algorithm.py
│   └─ visualizer.py
└── README.md
```

---

## ⚙️ Requirement & Instalasi

### Prasyarat Package

- numpy>=2.3.2
- plotly>=6.3
- matplotlib>=3.10.6

### Instalasi Package

1. Clone repository.

   ```bash
   git clone https://github.com/timoruslim/IF3170_G60_MoreArtificialThanIntelligence.git
   cd IF3170_G60_MoreArtificialThanIntelligence
   ```

2. Pasang dependensi.

   ```bash
   pip install -r requirements.txt
   ```

   Jika file `requirements.txt` belum ada, bisa install manual.

   ```bash
   pip install numpy matplotlib
   ```

---

## 🚀 Menggunakan Package

Cara kerja package dilihat di salah satu file `.ipynb` pada [`output`](output). Selain itu, berikut "tutorial" singkat.

### Trucks, Packages, and States

Suatu persoalan didefinisikan oleh larik `Truck` dan `Package`. Lalu, suatu `State` diinisialisasikan dari larik tersebut.

```python
from src import Truck, Package, State

trucks = [
   Truck("T1", 10, 20, 5, 200),
   Truck("T2", 8, 12, 4, 150),
]

packages = [
   Package("S1", 1, 1, 1, 50, 2, False, 1),
   Package("S2", 1, 2, 1, 45, 3, False, 3),
   Package("S3", 2, 1, 1, 40, 2, True, 2),
   Package("S4", 1, 1, 2, 35, 1, False, 4),
   Package("S5", 2, 2, 1, 55, 4, False, 1),
]

initial_state = State(packages, trucks, init="random_feasible")
```

### Objective and Solver

Untuk menyelesaikan persoalan yang telah dibuat, cukup memilih `ObjectiveFunction` dan `Solver` yang diinginkan.

```python
from src import MaxValueObjective, SimulatedAnnealing, RationalSchedule

objective = MaxValueObjective()

schedule = RationalSchedule(100, 0.001)
solver = SimulatedAnnealing(objective, schedule, max_iterations=10000)
result = solver.solve(initial_state)
```

## Results

Hasil yang dikembalikan suatu `Solver` dapat langsung di-_print_ (sudah terformat) atau divisualisasikan (dengan `draw_state`).

```python
from src import draw_state

print(result)
draw_state(result)
```

---

## 👨‍💻 Authors

| Nama                     | NIM      | Pembagian Tugas                                      |
| ------------------------ | -------- | ---------------------------------------------------- |
| Timothy Niels Ruslim     | 10123053 | representasi persoalan, simulated annealing, laporan |
| Theodore Marvel Suranton | 10623061 | hill climbing, analisis perbandingan, laporan        |
| Qodri Azkarayan          | 10823501 | genetic algorithm, bonus objektif, laporan           |

Bukti dapat dilihat dari sejarah _commits_.

---

## 🔗 Tautan

- 📂 [Repository GitHub](https://github.com/timoruslim/IF3170_G60_MoreArtificialThanIntelligence)

---

> Dibuat sebagai bagian dari Tugas Besar 1 IF3170 Inteligensi Artifisial 2026 – ITB
