import json
from colorama import init, Fore

init(autoreset=True)

# File path for JSON data
my_file = 'videos_data.json'

# Function to open file with error handling
def file_opener(file_name, open_in_mode):
    try:
        with open(file_name, open_in_mode) as f:
            return f.read()
    except FileNotFoundError:
        return '[]'

# Function to load JSON data
def load_data(data_json_file):
    file = file_opener(data_json_file, 'r')
    return json.loads(file)

# Function to save data to JSON file
def save_data(data_want_to_save, file_to_save_data):
    with open(file_to_save_data, 'w') as file:
        json.dump(data_want_to_save, file, indent=2)

# Function to list all videos
def list_videos(videos):
    print('*' * 70)
    if len(videos) == 0:
        print(Fore.RED + "No data available!")
    else:
        for index, vid in enumerate(videos):
            print(f"{index + 1}: {videos[index]['name']}, Duration: {videos[index]['Duration']}")
    print('*' * 70)

# Function to add a video
def add_video(videos):
    name = input("Enter video's title: ")
    duration = int(input("Enter video's duration: "))
    videos.append({'name': name, 'Duration': duration})
    save_data(videos, my_file)
    print(Fore.RED + "Addition is Successful!")

# Function to delete a video
def delete_video(videos):
    list_videos(videos)
    index = int(input("Index of video to be deleted: "))
    try:
        del videos[index - 1]
        list_videos(videos)
        save_data(videos, my_file)
        print(Fore.RED + "Deletion Successful!")
    except IndexError:
        print(Fore.RED + "Invalid index!")

# Function to update a video
def update_video(videos):
    list_videos(videos)
    index = int(input("Select index you want to update: "))
    try:
        name = input("Enter new video's title: ")
        duration = int(input("Enter new video's duration: "))
        videos[index - 1] = {'name': name, 'Duration': duration}
        list_videos(videos)
        save_data(videos, my_file)
        print(Fore.RED + "Updation Successful!")
    except IndexError:
        print(Fore.RED + "Invalid index!")

# Function to delete all videos
def delete_all(videos):
    warning = input(Fore.RED + "Type 'yes' to delete all videos: ")
    if warning == 'yes':
        videos.clear()
        print(Fore.RED + "All Data Removed Successfully!")
        save_data(videos, my_file)

# Main function
def main():
    while True:
        try:
            videos = load_data(my_file)
            print(Fore.RED + "\n YouTube Manager | Choose an option")
            print("1. List all YouTube videos")
            print("2. Add a YouTube video")
            print("3. Delete a YouTube video")
            print("4. Update a YouTube video")
            print("5. Delete all videos")
            print("6. Exit the app")
            choice = input("Enter your choice: ")

            match choice:
                case '1':
                    list_videos(videos)
                case '2':
                    add_video(videos)
                case '3':
                    delete_video(videos)
                case '4':
                    update_video(videos)
                case '5':
                    delete_all(videos)
                case '6':
                    break
                case _:
                    print(Fore.RED + 'Invalid Input!')
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")

# Calling the main function
if __name__ == "__main__":
    main()
