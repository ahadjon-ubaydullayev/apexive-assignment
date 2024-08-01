import csv


class CSVExporter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers

    def export(self, data):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
            for row in data:
                writer.writerow([row.get(header, '')
                                for header in self.headers])


# Use case for Aircraft table
headers = ['AircraftID', 'Make', 'Model', 'Complex', 'HighPerformance']
data = [
    {'AircraftID': '001', 'Make': 'Cessna', 'Model': '172',
        'Complex': False, 'HighPerformance': False},
    {'AircraftID': '002', 'Make': 'Piper', 'Model': 'Cherokee',
        'Complex': True, 'HighPerformance': True}
]
exporter = CSVExporter('aircrafts.csv', headers)
exporter.export(data)


# use case for Flights table
flight_headers = [
    "Date", "AircraftID", "From", "To", "Route", "TimeOut", "TimeOff", "TimeOn", "TimeIn",
    "OnDuty", "OffDuty", "TotalTime", "PIC", "SIC", "Night", "Solo", "CrossCountry", "NVG", "NVGOps",
    "Distance", "DayTakeoffs", "DayLandingsFullStop", "NightTakeoffs", "NightLandingsFullStop",
    "AllLandings", "ActualInstrument", "SimulatedInstrument", "HobbsStart", "HobbsEnd", "TachStart",
    "TachEnd", "Holds", "Approach1", "Approach2", "Approach3", "Approach4", "Approach5", "Approach6",
    "DualGiven", "DualReceived", "SimulatedFlight", "GroundTraining", "InstructorName", "InstructorComments",
    "Person1", "Person2", "Person3", "Person4", "Person5", "Person6", "FlightReview", "Checkride",
    "IPC", "NVGProficiency", "FAA6158", "CustomFieldName", "CustomNumericFieldName", "CustomHoursFieldName",
    "CustomCounterFieldName", "CustomDateFieldName", "CustomDateTimeFieldName", "CustomToggleFieldName", "PilotComments"
]

flights_data = [
    {
        "Date": "2023-01-01", "AircraftID": "123", "From": "ABC", "To": "XYZ", "Route": "Direct",
        "TimeOut": "0800", "TimeOff": "0830", "TimeOn": "0930", "TimeIn": "1000", "OnDuty": "0700",
        "OffDuty": "1100", "TotalTime": 1.5, "PIC": 1.5, "SIC": 0, "Night": 0, "Solo": 0,
        "CrossCountry": 1.5, "NVG": 0, "NVGOps": 0, "Distance": 150, "DayTakeoffs": 1, "DayLandingsFullStop": 1,
        "NightTakeoffs": 0, "NightLandingsFullStop": 0, "AllLandings": 1, "ActualInstrument": 0,
        "SimulatedInstrument": 0, "HobbsStart": 100, "HobbsEnd": 101.5, "TachStart": 200, "TachEnd": 201.5,
        "Holds": 0, "Approach1": "ILS", "Approach2": "", "Approach3": "", "Approach4": "",
        "Approach5": "", "Approach6": "", "DualGiven": 0, "DualReceived": 0, "SimulatedFlight": 0,
        "GroundTraining": 0, "InstructorName": "", "InstructorComments": "", "Person1": "John Doe",
        "Person2": "", "Person3": "", "Person4": "", "Person5": "", "Person6": "",
        "FlightReview": False, "Checkride": False, "IPC": False, "NVGProficiency": False,
        "FAA6158": False, "CustomFieldName": "Extra Info", "CustomNumericFieldName": 42,
        "CustomHoursFieldName": 3.5, "CustomCounterFieldName": 5, "CustomDateFieldName": "2023-01-02",
        "CustomDateTimeFieldName": "2023-01-02T15:00:00", "CustomToggleFieldName": True, "PilotComments": "Smooth flight."
    }
]

exporter = CSVExporter('flights.csv', flight_headers)
exporter.export(flights_data)
