import sys

# Sakamoto's algorithm - input date, month, year - output day in the week #
def dow(y, m, d) :
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7
# ----------------------------------------------------------------------- #

def main():
    try:
        while True:
     
            date = input("date >> ")
            month = input("month >> ")
            year = input("year >> ")
           
            print(dow(year, month, date));

    except KeyboardInterrupt:
        print "\nApplication exiting ..."
        sys.exit(0)

if __name__ == "__main__":
    main()
