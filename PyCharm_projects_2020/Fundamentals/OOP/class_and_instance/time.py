class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        if self.seconds + seconds <= Time.max_seconds:
            self.seconds += seconds
        else:
            self.seconds = self.seconds + seconds - 60
            self.minutes += 1
        if self.minutes + minutes <= Time.max_minutes:
            self.minutes += minutes
        else:
            self.minutes = self.minutes + minutes - 60
            self.hours += 1
        if self.hours + hours <= Time.max_hours:
            self.hours += hours
        else:
            self.hours = self.hours + hours - 24

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.set_time(0, 0, 1)
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
time = Time(22, 30, 10)
time.set_time(2, 35, 50)
print(time.get_time())