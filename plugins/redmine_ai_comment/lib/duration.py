class Duration:
    def __init__(self, minutes: int):
        self.all_minutes: int = minutes if minutes >= 0 else 0


    def as_minutes(self):
        return self.all_minutes
    
    
    def as_hours_and_minutes(self):
        hours = self.all_minutes // 60
        minutes = self.all_minutes % 60

        return hours, minutes
    
    
    def as_string(self):
        hours, minutes = self.as_hours_and_minutes()

        total = []

        if hours > 0:
            total.append(str(hours) + (" hour" if hours == 1 else " hours"))

        if minutes > 0:
            total.append(str(minutes) + (" minute" if minutes == 1 else " minutes"))

        if len(total) == 0:
            return "0 minutes"
        else:
            return " ".join(total)

