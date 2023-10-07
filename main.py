import datetime
import pandas as pd


def find_room(csv_data):
    data = pd.read_csv(csv_data)
    # hr = str(curr_hr)
    # create a list of new columns names and pass it to the original columns names
    col_names = ["RoomNo", "9", "10", "11", "12", "13", "14", "15", "16"]
    #     col_names = ["RoomNo",9,10,11,12,13,14,15,16]
    data.columns = col_names

    # Instead of renaming like this we can rename like above
    #     data1 = data.rename(columns={
    #         "9:30 - 10:20 AM":"9",
    #         "10:20 - 11:10 AM":"10",
    #         "11:10 - 12:00 PM":"11",
    #         "12:00 - 12:50 PM":"12",
    #         "1:00 - 1:50 PM":"1",
    #         "1:50 - 2:40 PM":"2",
    #         "2:40 - 3:30 PM":"3",
    #         "3:30 - 4:20 PM":"4"
    #     })

    #     data2 = data1.loc[(data['9:30 - 10:20 AM']==0)]
    #     data3 = data2.loc[:,("Room No.",'9:30 - 10:20 AM')]

    data1 = data.loc[(data["9"] == 0)]
    data2 = data1.loc[:, ("RoomNo", "9")]
    data3 = data2.reset_index(drop=True)
    print("All below listed room is vacant till 9:30 - 10:20 AM")
    for j in range(len(data3.index)):
        print(f"Room No {data3.loc[j, 'RoomNo']}")


current_day = datetime.datetime.now().strftime("%A").lower()
current_time = datetime.datetime.now()
current_hour = current_time.hour

# if current_day=='wednesday':
#     find_room()
# else:
#     print("No vacant room available")
match current_day:
    case "monday":
        print("case monday is going to execute")
        find_room("csvData/monday.csv")
        print("Execution of case monday after function call")

    case "tuesday":
        print("case tuesday is going to execute")
        find_room("csvData/tuesday.csv")
        print("Execution of case tuesday after function call")

    case "wednesday":
        print("case wednesday is going to execute")
        find_room("csvData/wednesday.csv")
        print("Execution of case wednesday after function call")

    case "thursday":
        print("case thursday is going to execute")
        find_room("csvData/thursday.csv")
        print("Execution of case thursday after function call")

    case "friday":
        print("case friday is going to execute")
        find_room("csvData/friday.csv")
        print("Execution of case friday after function call")

    case "saturday":
        print("case saturday is going to execute")
        find_room("csvData/saturday.csv")
        print("Execution of case saturday after function call")

    case default:
        print("Default case executed")
