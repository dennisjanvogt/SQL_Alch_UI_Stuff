from models import Pokemon


if __name__ == "__main__":
    bisasam = Pokemon(name="Bisasam", typ="Pflanze", level=8)
    bisasam.save_to_db()
