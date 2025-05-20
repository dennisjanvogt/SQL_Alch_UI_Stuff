from models import Pokemon

if __name__ in {"__main__", "__mp_main__"}:
    glu = Pokemon("Glurak", "Feuer", level=50)
    print(glu.id)
    glu.save_to_db()
    print(glu.id)
    glu.level = 59
    glu.update_at_db()
