import os
import shutil
from datetime import datetime


class FileOrganizer:

    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".doc", ".docx", ".txt"],
            "PDFs": [".pdf"]
        }

        self.count = {
            "Images": 0,
            "Documents": 0,
            "PDFs": 0,
            "Others": 0
        }

        self.total_files = 0
        self.moved_files = []

    def get_category(self, extension):
        extension = extension.lower()

        for category, extensions in self.categories.items():
            if extension in extensions:
                return category

        return "Others"

    def organize_files(self):
        try:
            if not os.path.exists(self.destination_folder):
                os.makedirs(self.destination_folder)

            for file in os.listdir(self.source_folder):

                source_path = os.path.join(self.source_folder, file)

                if os.path.isfile(source_path):

                    extension = os.path.splitext(file)[1]
                    category = self.get_category(extension)

                    category_folder = os.path.join(
                        self.destination_folder, category)

                    os.makedirs(category_folder, exist_ok=True)

                    destination_path = os.path.join(category_folder, file)

                    shutil.move(source_path, destination_path)

                    self.total_files += 1
                    self.count[category] += 1
                    self.moved_files.append(f"{file} --> {category}")

        except Exception as e:
            print("Error:", e)

    def generate_report(self):
        try:
            with open("report.txt", "w") as report:

                report.write("FILE ORGANIZER REPORT\n")
                report.write("=" * 30 + "\n\n")

                report.write("Timestamp: ")
                report.write(str(datetime.now()))
                report.write("\n\n")

                report.write(f"Total Files: {self.total_files}\n\n")

                report.write("Files by Category:\n")
                report.write(f"Images: {self.count['Images']}\n")
                report.write(f"Documents: {self.count['Documents']}\n")
                report.write(f"PDFs: {self.count['PDFs']}\n")
                report.write(f"Others: {self.count['Others']}\n\n")

                report.write("Moved Files:\n")

                for file in self.moved_files:
                    report.write(file + "\n")

            print("Report saved successfully.")

        except Exception as e:
            print("Error:", e)