from nicegui import ui
from models import Pokemon

global pokis


def speichern():
    poki = Pokemon(name=input_name.value, typ=input_typ.value, level=input_level.value)
    poki.save_to_db()

    input_typ.value = None
    input_name.value = None
    input_level.value = None
    global pokis
    pokis = Pokemon.get_all_poki()
    tabelle.rows = [{"name": p.name, "typ": p.typ, "level": p.level} for p in pokis]


with ui.tabs().classes("w-full") as tabs:
    one = ui.tab("Speichern")
    two = ui.tab("Laden")
with ui.tab_panels(tabs, value=one):
    with ui.tab_panel(one):
        input_name = ui.input(label="Name")
        input_typ = ui.input(label="Typ")
        input_level = ui.input(label="Level")
        ui.button(icon="save", text="Speichern", on_click=lambda: speichern())
    with ui.tab_panel(two):
        pokis = Pokemon.get_all_poki()
        tabelle = ui.table(
            rows=[{"name": p.name, "typ": p.typ, "level": p.level} for p in pokis]
        )


ui.run()
