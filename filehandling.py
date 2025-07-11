"""with open("file.txt") as f:
  print(f.readline(50))

with open("file.txt","a") as f:
  f.write("Hello")

with open("file.txt", "w") as f:
  f.write("Hello! world")"""


def main():
    my_file = open('books.txt', 'w')

    try:
      my_file.write('If Tomorrow Comes by Sidney Sheldon')
    except Exception as e:
      print(f'writing to file failed: {e}')
    finally:
      my_file.close()

if __name__ == '__main__':
  main()