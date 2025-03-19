import os
import shutil
from datetime import datetime

class FileProcessor:
    """
    FileProcessor that processes the file synchronously
    """
    def process_file(self, file_path, specializations, exam_parts, file_types, year, period) -> str:
        """
        Processes the specified file in four steps:
            1. Check if the file exists
            2. Generate a new filename based on the current date
            3. Create the destination directory structure if needed
            4. Move and rename the file

        :param file_path: Path of the file to process
        :param specializations: Selected specialization
        :param exam_parts: Selected exam part
        :param file_types: Selected file type
        :param year: Selected year
        :param period: Selected period
        :return: New path of the processed file
        """
        print(f"Started processing file: {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        print("Generating filename...")
        original_filename = os.path.basename(file_path)
        file_extension = os.path.splitext(original_filename)[1].lower()
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        new_filename = f"{file_types}_{date}{file_extension}"

        print("Creating destination directory...")
        original_directory = os.path.dirname(file_path)
        base_destination = os.path.join(original_directory, specializations, exam_parts, year, period)
        os.makedirs(base_destination, exist_ok=True)

        print("Moving and renaming the file...")
        destination_path = os.path.join(base_destination, new_filename)
        shutil.move(file_path, destination_path)
        print(f"File renamed and moved to: {destination_path}")

        return destination_path