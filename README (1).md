# 🎬 YOLO — OTT Platform Management System

A Python-based desktop application for managing an OTT (Over-The-Top) streaming platform. The system provides both a **console-based interface** (`MAIN MENU.py`) and a **graphical user interface** (`GUI.py`) for managing movies, series, workforce, memberships, transactions, analytics, and visualisations.

---

## 📁 Project Directory Structure

```
D:\OTT Platform Management\
│
├── MAIN MENU.py          # Console-based application (original)
├── GUI.py                # Tkinter GUI application
│
├── MOVIES.csv            # Movie records database
├── SERIES.csv            # Series records database
├── MEMBERSHIP.csv        # Member records database
├── TRANSACTIONS.csv      # Transaction/payment records
├── WORKFORCE.csv         # Employee records database
│
└── .gitignore            # Git ignore rules
```

---

## ⚙️ Requirements

### Python Version
- Python 3.8 or above

### Libraries
Install the required libraries using pip:

```bash
pip install pandas numpy matplotlib
```

> `tkinter` comes **built-in** with Python on Windows. No separate installation needed.

---

## 🚀 How to Run

### GUI Version (Recommended)
```bash
python GUI.py
```

### Console Version
```bash
python "MAIN MENU.py"
```

---

## 📋 CSV File Structure

The application reads from and writes to the following CSV files. Make sure all files exist at `D:\OTT Platform Management\` before running.

### MOVIES.csv
| Column | Description |
|---|---|
| ID | Unique movie ID |
| TITLE | Movie title |
| RELEASE DATE | Release date (DD-MM-YYYY) |
| LANGUAGE | Available languages |
| PRODUCER | Producer name |
| CERTIFICATE | Age certificate (U, UA, A, etc.) |
| COUNTRY | Country of origin |
| GENRE | Movie genre |
| DURATION | Duration label |
| RUNTIME | Runtime in minutes |
| RATING | IMDB rating |
| GROSS | Box office gross amount |

### SERIES.csv
| Column | Description |
|---|---|
| Sr.No | Serial number |
| Title | Series title |
| Ratings | Audience rating |
| Language | Available languages |
| Release Date | Release date (DD-MM-YYYY) |
| Genre | Series genre |
| Runtime | Runtime per episode |
| Episodes | Total number of episodes |
| Gross | Total gross amount |
| Seasons | Total number of seasons |

### WORKFORCE.csv
| Column | Description |
|---|---|
| S-ID | Employee ID |
| NAME | Employee name |
| CONTACT | Contact number |
| SALARY | Monthly salary |
| GENDER | Gender |
| POST | Job title / designation |

### MEMBERSHIP.csv
| Column | Description |
|---|---|
| M-ID | Member ID |
| NAME | Member name |
| MEMBERSHIP PLAN | Plan type (A / B / C) |

### TRANSACTIONS.csv
| Column | Description |
|---|---|
| M-ID | Transaction ID |
| DATE | Transaction date |
| NAME | Member name |
| MEMBERSHIP TYPE | Plan type (A / B / C) |
| MEMBERSHIP PLAN | Plan name (SILVER / GOLD / PLATINUM) |
| START DATE | Subscription start date |
| END DATE | Subscription end date |
| METHOD OF PAYMENT | CARD or NET BANKING |
| TOTAL | Amount paid |

---

## 💳 Membership Plans

| Type | Plan | Price | Duration |
|---|---|---|---|
| A | SILVER | ₹199 | 30 Days |
| B | GOLD | ₹699 | 180 Days |
| C | PLATINUM | ₹1,669 | 365 Days |

---

## 🖥️ Features

### Movies
- Display all movie records
- Add new movie
- Update existing movie by ID
- Delete movie by ID
- Search movie by title

### Series
- Display all series records
- Add new series
- Update existing series by Sr.No
- Delete series by Sr.No
- Search series by title

### Workforce
- Display all employee records
- Add new employee
- Update employee details by S-ID
- Delete employee by S-ID
- Search employee by name

### Membership
- Display all member records
- Update member record by M-ID
- Search member by name

### Transactions
- Apply for new membership (generates receipt)
- Renew existing membership (generates receipt)
- Cancel membership

### Analytics
- **Movies:** Max/Min runtime by country, gross by genre, ratings by language and year
- **Series:** Max/Min runtime and ratings by year, gross and seasons by genre
- **Plans:** Most and least popular membership plan

### Visualisation
- **Movies:** Ratings by year (line), Gross by genre, Ratings by language, Gross by certificate, Country by runtime, Duration histogram
- **Series:** Genre vs Gross, Language vs Gross, Language vs Runtime, Ratings vs Genre
- **Plans & Members:** Plan frequency, Revenue per plan, Payment method frequency

---

## 🛠️ Known Limitations

- All CSV file paths are **hardcoded** to `D:\OTT Platform Management\`. If you move the project folder, update the `BASE_PATH` variable at the top of `GUI.py`.
- The console version (`MAIN MENU.py`) uses recursive function calls for navigation, which may hit Python's recursion limit on extended use.
- No login/authentication system is implemented.
- No database backend — all data is stored in flat CSV files.

---

## 📌 Notes

- Always ensure the CSV files are present and correctly formatted before launching the application.
- When adding records, ID/Sr.No columns are **auto-incremented** — do not enter them manually.
- Dates should be entered in `DD-MM-YYYY` format.
- Membership plan types must be entered as `A`, `B`, or `C` (uppercase).
- Payment method must be entered as `CARD` or `NET BANKING` (uppercase).

---

## 👨‍💻 Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| GUI Framework | Tkinter |
| Data Handling | Pandas, NumPy |
| Visualisation | Matplotlib |
| Storage | CSV Files |

---

*Project: YOLO OTT Platform Management System*
