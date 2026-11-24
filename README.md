# Todo Django

**[English](#english)** | **[Srpski](#srpski)**

---

## English

A simple to-do list app built with Django, with user registration and login. Each user sees only their own tasks.

### Features

- Sign up for a new account (username must be unique, password at least 5 characters)
- Log in and log out
- Add tasks
- Mark a task as done
- Delete tasks
- Django admin panel at `/admin/`

### Getting started

Requires Python 3.10 or newer.

```bash
git clone https://github.com/Migul123/todo-django.git
cd todo-django

python -m venv venv
venv\Scripts\activate        # on Linux/macOS: source venv/bin/activate
pip install -r requirements.txt

cd todoprj
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/ and sign up.

To use the admin panel, create an admin account:

```bash
python manage.py createsuperuser
```

### Project structure

```
todoprj/
├── todoprj/        # project settings (settings.py, urls.py)
└── todoapp/        # the app: models, views, templates
    └── templates/todoapp/   # login.html, register.html, todo.html
projekat.py         # separate people-detection script (see below)
```

### People detection (`projekat.py`)

A separate script, not part of the to-do app. It uses a YOLOv8 model to find people in a video and draws green boxes around them.

- The `yolov8n.pt` model is downloaded automatically on first run.
- The `primer.mp4` video is not included in the repository. Put your own video next to the script under that name.
- Press `Esc` to close the window.

```bash
python projekat.py
```

### Production note

`SECRET_KEY` is read from the `DJANGO_SECRET_KEY` environment variable. The app runs locally without it, but before deploying to a server, set your own key and turn off `DEBUG`.

---

## Srpski

Jednostavna aplikacija za listu zadataka napravljena u Django-u, sa registracijom i prijavom korisnika. Svaki korisnik vidi samo svoje zadatke.

### Funkcionalnosti

- Registracija novog naloga (korisničko ime mora biti jedinstveno, lozinka najmanje 5 karaktera)
- Prijava i odjava
- Dodavanje zadataka
- Označavanje zadatka kao završenog
- Brisanje zadataka
- Django admin panel na `/admin/`

### Pokretanje

Potreban je Python 3.10 ili noviji.

```bash
git clone https://github.com/Migul123/todo-django.git
cd todo-django

python -m venv venv
venv\Scripts\activate        # na Linux/macOS: source venv/bin/activate
pip install -r requirements.txt

cd todoprj
python manage.py migrate
python manage.py runserver
```

Zatim otvori http://127.0.0.1:8000/ i registruj se.

Za pristup admin panelu napravi administratorski nalog:

```bash
python manage.py createsuperuser
```

### Struktura projekta

```
todoprj/
├── todoprj/        # podešavanja projekta (settings.py, urls.py)
└── todoapp/        # aplikacija: modeli, view-ovi, šabloni
    └── templates/todoapp/   # login.html, register.html, todo.html
projekat.py         # zasebna skripta za detekciju osoba (vidi ispod)
```

### Detekcija osoba (`projekat.py`)

Zasebna skripta, nije deo todo aplikacije. Koristi model YOLOv8 da pronađe osobe u video snimku i označi ih zelenim pravougaonicima.

- Model `yolov8n.pt` se automatski preuzima pri prvom pokretanju.
- Video `primer.mp4` nije uključen u repozitorijum. Stavi svoj snimak pod tim imenom pored skripte.
- Taster `Esc` zatvara prozor.

```bash
python projekat.py
```

### Napomena za produkciju

`SECRET_KEY` se čita iz promenljive okruženja `DJANGO_SECRET_KEY`. Lokalno aplikacija radi i bez nje, ali pre postavljanja na server obavezno postavi sopstveni ključ i isključi `DEBUG`.
