import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from app.models import Base

load_dotenv()
db_url = os.environ['DATABASE_URL']
engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)
print("Tables created.")
