from models.base.database import db
from sqlalchemy import Index, String
from sqlalchemy.orm import Mapped, mapped_column


class Exportacao(db.Model):
    __tablename__ = "exportacao"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    dataset_id: Mapped[int] = mapped_column(nullable=False)
    dataset_nome: Mapped[str] = mapped_column(String(64), nullable=False)
    tipo: Mapped[str] = mapped_column(String(64), nullable=False)
    pais: Mapped[str] = mapped_column(String(128), nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    quantidade: Mapped[int] = mapped_column(nullable=False)
    valor: Mapped[int] = mapped_column(nullable=False)

    __table_args__ = (Index("exportacao_search", "dataset_nome", "ano"),)

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "ano": self.ano,
            "pais": self.pais,
            "quantidade": self.quantidade,
            "valor": self.valor,
        }
