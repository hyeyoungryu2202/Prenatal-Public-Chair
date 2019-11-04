from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://zqohhemoyreaxt:b0008668d9e5d0ecb143bfd962b083d712bcc07ff63b5177758aad9f5d8d7cbb@ec2-23-21-220-23.compute-1.amazonaws.com:5432/d3lubmbeuro8nv', encoding = 'utf-8', echo=True)



db_session = scoped_session(sessionmaker(autocommit = False,
                                         autoflush = False,
                                         bind = engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  import models
  Base.metadata.create_all(bind=engine)


