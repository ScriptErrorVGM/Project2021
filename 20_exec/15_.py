def main():
    i = "white-green-red-blue-yellow"
    n = i.split('-') 
    n.sort()
    print('-'.join(n))
  

if __name__ == "__main__":
    main()