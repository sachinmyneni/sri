import sqlite3

if __name__ == '__main__':
  con = sqlite3.connect('sensor_data.db')
  cur = con.cursor()
  cur.execute('SELECT name FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%"')
  print(cur.fetchall())
  cur.execute('SELECT * FROM sqlite_master')
  print(cur.description)
  cur.execute('select * from sensor_data')
  print(cur.fetchall())
  cur.execute('select * from sensor_data WHERE date < "20210102"')
  print(cur.fetchall())

