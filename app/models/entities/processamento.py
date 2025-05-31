from models.base.database import db
from sqlalchemy import Index, String
from sqlalchemy.orm import Mapped, mapped_column


class Processamento(db.Model):
    __tablename__ = "processamento"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    dataset_id: Mapped[int] = mapped_column(nullable=False)
    dataset_nome: Mapped[str] = mapped_column(String(64), nullable=False)
    tipo: Mapped[str] = mapped_column(String(64), nullable=False)
    control: Mapped[str] = mapped_column(String(64), nullable=False)
    cultivar: Mapped[str] = mapped_column(String(128), nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    quantidade: Mapped[int] = mapped_column(nullable=False)

    __table_args__ = (Index("processamento_search", "dataset_nome", "ano"),)

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "ano": self.ano,
            "cultivar": self.cultivar,
            "quantidade": self.quantidade,
        }
