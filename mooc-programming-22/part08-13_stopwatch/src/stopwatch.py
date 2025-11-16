# Write your solution here: 
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
 
    def tick(self):
        if self.minutes == 59 and self.seconds == 59:
            self.minutes = 0
            self.seconds = 0
 
        elif self.seconds == 59:
            self.minutes += 1
            self.seconds = 0
 
        else:
            self.seconds += 1
 
    def __str__(self):
        if self.seconds < 10:
            the_seconds = f"0{self.seconds}"
        else:
            the_seconds = f"{self.seconds}"

        if self.minutes < 10:
            the_minutes = f"0{self.minutes}"
        else:
            the_minutes = f"{self.minutes}"
        
        return f"{the_minutes}:{the_seconds}"
 
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(10):
        print(watch)
        watch.tick()


# Answers!!!
# class Stopwatch:
#     def __init__(self):
#         self.seconds = 0
#         self.minutes = 0
 
#     def tick(self):
#         self.seconds += 1
#         if self.seconds == 60:
#             self.seconds = 0
#             self.minutes += 1
#             if self.minutes == 60:
#                 self.minutes = 0
 
#     def __str__(self):
#         return f"{self.minutes:02}:{self.seconds:02}"