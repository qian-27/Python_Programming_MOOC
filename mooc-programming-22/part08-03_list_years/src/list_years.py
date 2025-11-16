# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date
def list_years(dates: list):
   year_list = []
   new_year = 0
   for item in dates:
      new_year = item.year
      year_list.append(new_year)
   list_in_order = sorted(year_list)
   return list_in_order


# You can test your function by calling it within the following block
if __name__ == "__main__":
   date1 = date(2019, 2, 3)
   date2 = date(2006, 10, 10)
   date3 = date(1993, 5, 9)

   years = list_years([date1, date2, date3])
   print(years)



# from datetime import date
 
# def list_years(dates: list):
#     years = []
#     for dt in dates:
#         years.append(dt.year)
 
#     years.sort()
#     return years
 