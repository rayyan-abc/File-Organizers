from organizer import FileOrganizer

source_folder = "sample_files"
destination_folder = "organized_files"

organizer = FileOrganizer(source_folder, destination_folder)

organizer.organize_files()
organizer.generate_report()

print("Files organized successfully.")
print("Report saved as report.txt")