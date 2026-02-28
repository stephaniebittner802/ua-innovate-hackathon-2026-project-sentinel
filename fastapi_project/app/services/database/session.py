
import os
from sqlalchemy.engine.url import make_url
from sqlmodel import create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

url = make_url(DATABASE_URL)
is_sqlite = url.get_backend_name().startswith("sqlite")

connect_args = {"check_same_thread": False} if is_sqlite else {}

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_size=5 if not is_sqlite else None,
    max_overflow=10 if not is_sqlite else None,
    connect_args=connect_args,
)

def get_session():
    with Session(engine) as session:
        yield session
