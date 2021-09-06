from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Favourite Countries" table
class Favourite_Countries(base):
    __tablename__ = "Favourite_Countries"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)
    language = Column(String)
    famous_for = Column(String)

  
# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records for our Favourite_Countries table
cambodia = Favourite_Countries(
    country_name="Cambodia",
    capital_city="Phnom Penh",
    language="Khmer",
    population=5000000,
    famous_for="Angkor Wat"
)


# add each instance of our favourite_countries to our session
session.add(cambodia)


# commit our session to the database
session.commit()

# query the database to find all programmers
favourite_countries = session.query(Favourite_Countries)
for country in favourite_countries:
    print(
        country.id,
        country.country_name,
        country.population,
        country.language,
        country.famous_for,
        sep=" | "
        
    )