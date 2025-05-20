from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, String, Integer

engine = create_engine("sqlite:///pokemon.db", echo=False)


class Base(DeclarativeBase):
    pass


class PokemonORM(Base):
    __tablename__ = "pokemon"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    typ: Mapped[str] = mapped_column(String(30))
    level: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Pokemon(id={self.id!r}, name={self.name!r}, typ={self.typ!r}, lvl={self.level!r})"


Base.metadata.create_all(engine)
