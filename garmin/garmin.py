# import necessary libraries
import csv, re
from tabulate import tabulate
from datetime import datetime

#define main function
def main():
    # set variable to the saved csv file in the same directory
    csv_file_path = '/workspaces/143379034/garmin/garmin.csv'
    #print(csv_file_path)
    #activity_objects = from_csv(csv_file_path)
    #for activity in activity_objects:
    #    print(f"Activity Type: {activity.activity_type}, Date: {activity.date}, Distance: {activity.distance}, Calories: {activity.calories}, Time: {activity.time}, Avg HR: {activity.avg_hr}, Max HR: {activity.max_hr}")
    activities = from_csv(csv_file_path)
    to_csv(activities, 'output_garmin.csv')
    # convert csv into a usable format for tabulate
    file_path = '/workspaces/143379034/garmin/output_garmin.csv'
    data = convert_csv(file_path)

    # tabulate the table and print
    print(data)


def from_csv(csvFile):
    with open(csvFile, 'r') as file:
        reader = csv.DictReader(file)
        activities = []
        for row in reader:
            # Convert relevant values to the appropriate types
            activity_type = str(row['Activity Type'])
            title = str(row['Title'])
            distance = float(row['Distance'])
            calories = int(row['Calories'])
            time_elapsed = row['Time']
            avg_hr = int(row['Avg HR'])
            max_hr = int(row['Max HR'])

            # Create an instance of the Activity class for each row
            activity = Activity(
                activity_type=activity_type,
                date=row['Date'],
                favorite=row['Favorite'] == "true",
                title=title,
                distance=distance,
                calories=calories,
                time=time_elapsed,
                avg_hr=avg_hr,
                max_hr=max_hr,
                # Include other attributes as needed
            )

            # Append the created activity to the list
            activities.append(activity)

    return activities


def to_csv(activities, csvFile):
    with open(csvFile, 'w', newline='') as file:
        fieldnames = ['Date', 'Activity Type', 'Favorite', 'Title', 'Distance', 'Calories', 'Time', 'Avg HR', 'Max HR']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write each activity to the CSV file
        for activity in activities:
            writer.writerow({
                'Date': activity.date,
                'Activity Type': activity.activity_type,
                'Favorite': str(activity.favorite).lower(),
                'Title': activity.title,
                'Distance': activity.distance,
                'Calories': activity.calories,
                'Time': activity.time,
                'Avg HR': activity.avg_hr,
                'Max HR': activity.max_hr,
                # Include other attributes as needed
            })


# function to extract csv data and formulate into tabulate usable form
def convert_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        table = tabulate(reader, headers="firstrow", tablefmt="grid")
    return table


# define object code for an activity
class Activity:
    def __init__(self, activity_type=None, date=None, favorite=False, title=None, distance=None, calories=None, time=None, avg_hr=None, max_hr=None, aerobic_TE=None, avg_run_cadence=None, avg_pace=None, best_pace=None, total_ascent=None, total_descent=None, avg_stride_length=None, avg_vertical_ratio=None, avg_vertical_oscillation=None, avg_ground_contact_time=None, avg_gct_balance=None, training_stress_score=None, avg_power=None, max_power=None, grit=None, flow=None, total_strokes=None, avg_swolf=None, avg_stroke_rate=None, total_reps=None, dive_time=None, min_temp=None, surface_interval=None, decompression=None, best_lap_time=None, number_of_laps=None, max_temp=None, moving_time=None, elapsed_time=None, min_elevation=None, max_elevation=None):
        self.activity_type = activity_type
        self.date = date
        self.favorite = favorite
        self.title = title
        self.calories = calories
        self.distance = distance
        self.time = time
        self.avg_hr = avg_hr
        self.max_hr = max_hr
        self.aerobic_TE = aerobic_TE
        self.avg_run_cadence = avg_run_cadence
        self.avg_pace = avg_pace
        self.best_pace = best_pace
        self.total_ascent = total_ascent
        self.total_descent = total_descent
        self.avg_stride_length = avg_stride_length
        self.avg_vertical_ratio = avg_vertical_ratio
        self.avg_vertical_oscillation = avg_vertical_oscillation
        self.avg_ground_contact_time = avg_ground_contact_time
        self.avg_gct_balance = avg_gct_balance
        self.training_stress_score = training_stress_score
        self.avg_power = avg_power
        self.max_power = max_power
        self.grit = grit
        self.flow = flow
        self.total_strokes = total_strokes
        self.avg_swolf = avg_swolf
        self.avg_stroke_rate = avg_stroke_rate
        self.total_reps = total_reps
        self.dive_time = dive_time
        self.min_temp = min_temp
        self.surface_interval = surface_interval
        self.decompression = decompression
        self.best_lap_time = best_lap_time
        self.number_of_laps = number_of_laps
        self.max_temp = max_temp
        self.moving_time = moving_time
        self.elapsed_time = elapsed_time
        self.min_elevation = min_elevation
        self.max_elevation = max_elevation


    @property
    def activity_type(self):
        return self._activity_type


    @activity_type.setter
    def activity_type(self, activityName):
        self._activity_type = activityName


    @property
    def date(self):
        return self._date


    @date.setter
    def date(self, activityDateIn):
        self._date = activityDateIn


    @property
    def title(self):
        return self._title


    @title.setter
    def title(self, titleName):
        if titleName is not None and not isinstance(titleName, str):
            raise ValueError("Title must be a string.")
        self._title = titleName


    @property
    def distance(self):
        return self._distance


    @distance.setter
    def distance(self, distanceInMiles):
        if distanceInMiles is isinstance(distanceInMiles, float):
            raise ValueError("Distance must be a float.")
        self._distance = distanceInMiles


    @property
    def calories(self):
        return self._calories


    @calories.setter
    def calories(self, caloriesBurned):
        if caloriesBurned is isinstance(caloriesBurned, int):
            raise ValueError("Calories must be an integer.")
        self._calories = caloriesBurned


    @property
    def time(self):
        return self._time


    @time.setter
    def time(self, timeElapsed):
        timePattern = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
        if timeElapsed is not None and not timePattern.match(timeElapsed):
            raise ValueError("Incorrect time format.")
        self._time = timeElapsed


    @property
    def avg_hr(self):
        return self._avg_hr


    @avg_hr.setter
    def avg_hr(self, avgHR):
        if avgHR is isinstance(avgHR, int):
            raise ValueError("Calories must be an integer.")
        self._avg_hr = avgHR


    @property
    def max_hr(self):
        return self._max_hr


    @max_hr.setter
    def max_hr(self, maxHR):
        if maxHR is isinstance(maxHR, int):
            raise ValueError("Calories must be an integer.")
        self._max_hr = maxHR


class FitnessDay:
    def __init__(self, date='Today', steps=None):
        self.date = date
        self.steps = steps
        self.activities = []


#call main function
if __name__ == "__main__":
    main()
