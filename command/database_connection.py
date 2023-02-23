def database_connection(db_url: str = "") -> None:
    if db_url == "":
        print("No DB_URL provided")
    else:
        print(f"Connect to db {db_url}")
