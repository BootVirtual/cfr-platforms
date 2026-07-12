from cfr_platforms import logic
from prettytable import PrettyTable

data = logic.get_station_data("BucurestiNord")

arrivals_table = PrettyTable()

arrivals_table.field_names = ["Train", "No.", "From", "Operator", "Time", "Delay (min.)", "Platform"]
for row in data["arrivals"]:
    arrivals_table.add_row([row["type"], row["number"], row["destination"], row["operator"], row["time"], row["delay"], row["platform"]])

print("ARRIVALS:")
print(arrivals_table)


departures_table = PrettyTable()

departures_table.field_names = ["Train", "No.", "Destination", "Operator", "Time", "Delay (min.)", "Platform"]
for row in data["departures"]:
    departures_table.add_row([row["type"], row["number"], row["destination"], row["operator"], row["time"], row["delay"], row["platform"]])

print("DEPARTURES:")
print(departures_table)