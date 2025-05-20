from sqlalchemy.orm import Session
from db import PokemonORM, engine
from sqlalchemy import select


class Pokemon:

    def __init__(self, name, typ, level):
        self.name = name
        self.typ = typ
        self.level = level

    def save_to_db(self):
        with Session(engine) as session:
            poki = PokemonORM(name=self.name, typ=self.typ, level=self.level)

            session.add(poki)
            session.commit()

    @classmethod
    def get_all_poki(cls):
        with Session(engine) as session:
            all_poki = session.execute(select(PokemonORM))
            return [Pokemon(p.name, p.typ, p.level) for p in all_poki.scalars()]
