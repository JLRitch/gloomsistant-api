# standard modules
import pathlib as pl
import sqlite3

db_folder = pl.Path().cwd().joinpath("db")
db_path = db_folder.joinpath("db-dev.sqlite")

# main object to import from this module
db_conn = sqlite3.connect(db_path)