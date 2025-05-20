from sqlalchemy.orm import Session
from db import PokemonORM, engine
from sqlalchemy import select


class Pokemon:

    def __init__(self, name, typ, level, id=None):
        self.name = name
        self.typ = typ
        self.level = level
        self.id = id

    def __repr__(self) -> str:
        return f"Pokemon(id={self.id!r}, name={self.name!r}, typ={self.typ!r}, lvl={self.level!r})"

    def save_to_db(self):
        with Session(engine) as session:
            poki = PokemonORM(name=self.name, typ=self.typ, level=self.level)
            session.add(poki)
            session.commit()
            self.id = poki.id

    def delete_at_db(self):
        if self.id:
            raise Exception("Pokemon existiert noch nicht in der dB.")
        with Session(engine) as session:
            poki = session.query(PokemonORM).get(self.id)
            session.delete(poki)
            session.commit()

    def update_at_db(self):
        if self.id:
            raise Exception("Pokemon existiert noch nicht in der dB.")
        with Session(engine) as session:
            poki: PokemonORM = session.query(PokemonORM).get(self.id)
            poki.name = self.name
            poki.typ = self.typ
            poki.level = self.level
            session.add(poki)
            session.commit()

    @classmethod
    def get_all_poki(cls):
        with Session(engine) as session:
            all_poki = session.execute(select(PokemonORM))
            return [
                Pokemon(id=p.id, name=p.name, typ=p.typ, level=p.level)
                for p in all_poki.scalars()
            ]
