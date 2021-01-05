import sqlite3

if __name__ == '__main__':
  con = sqlite3.connect('sensor_data.db')
  cur = con.cursor()
  cur.execute('select * from sensor_data')
  print(cur.fetchall())
  cur.execute('select * from sensor_data WHERE date < "20210102"')
  print(cur.fetchall())

