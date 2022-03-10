from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


# #create
# def create_heroes():  
#     hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")  
#     hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
#     hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

#     with Session(engine) as session:  
#         session.add(hero_1)  
#         session.add(hero_2)
#         session.add(hero_3)

#         session.commit()  

# #read
# def select_heroes():
#     with Session(engine) as session:
#         statement = select(Hero).where(Hero.name == "Deadpond")#filter
#         results = session.exec(statement)
#         for hero in results:
#             print(hero)


# def update_heroes():
#     with Session(engine) as session:
#         statement = select(Hero).where(Hero.name == "Spider-Boy")
#         results = session.exec(statement)
#         hero = results.one()
#         print("Hero:", hero)

#         hero.age = 16
#         session.add(hero)
#         session.commit()
#         session.refresh(hero)
#         print("Updated hero:", hero)


def delete_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")  
        results = session.exec(statement)   
        hero = results.one()   
        print("Hero: ", hero)   

        session.delete(hero)   
        session.commit()   
        #print the deleted hero
        print("Deleted hero:", hero)  
        #query the db again
        statement = select(Hero).where(Hero.name == "Deadpond")   
        results = session.exec(statement)   
        hero = results.first()   
        #validation
        if hero is None:  
            print("There's no hero named Deadpond")   

def main():   
    # create_db_and_tables()  
    # create_heroes()  
    # select_heroes()
    # update_heroes()
    delete_heroes()


if __name__ == "__main__":  
    main()