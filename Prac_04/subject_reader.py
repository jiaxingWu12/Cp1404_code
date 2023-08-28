FILENAME = "subject_data.txt"

def main():
    data = get_data()
    display_subject_details(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Convert student count to integer
            data_list.append(parts)  # Add the parts to our data_list
    return data_list

def display_subject_details(data):
    """Display subject details in the required format."""
    for subject_detail in data:
        subject, lecturer, student_count = subject_detail
        print(f"{subject} is taught by {lecturer} and has {student_count} students")

if __name__ == "__main__":
    main()
