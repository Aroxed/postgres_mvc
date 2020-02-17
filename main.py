from model import Model

if __name__ == "__main__":
    the_model = Model()
    the_model.drop_table()
    the_model.create_table()
    the_user = {"name": "n1", "email": "email@server.com", "age": 20}
    the_model.insert(the_user)
    print(the_model.select_all())
    the_model.close()
