# CSV Analysis Project

This Django application allows users to upload CSV files, process them, and display various data visualizations and statistics.

## Features

- Upload CSV files.
- Display the first few rows of the uploaded data.
- Calculate and display summary statistics (mean, median, standard deviation) for numerical columns.
- Identify and handle missing values.
- Generate basic plots (histograms) for numerical columns and display them on the web page.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 3.2+
- pandas
- matplotlib
- seaborn (optional, if used for additional plotting)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/csv_analysis_project.git
    cd csv_analysis_project
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Open your web browser and go to:**

    ```
    http://127.0.0.1:8000/
    ```

### File Structure

- `csv_analysis_project/`: Main project directory.
- `csv_analysis/`: Django app handling CSV uploads and data processing.
- `csv_analysis/templates/`: HTML templates for the web pages.
- `csv_analysis/views.py`: Contains the view logic for file uploads and data processing.
- `csv_analysis/forms.py`: Form handling for CSV file uploads.
- `csv_analysis_project/settings.py`: Django project settings.
- `csv_analysis_project/urls.py`: URL routing for the project.

### Brief Explanation

This project is designed to help users upload and analyze CSV files. Users can upload a CSV file, and the application will process the file to display the first few rows of data. Additionally, it calculates summary statistics such as mean, median, and standard deviation for numerical columns. The application also identifies and handles missing values. Finally, it generates basic plots (such as histograms) for numerical columns and displays them on the web page.

### Example Usage

1. **Upload a CSV file:**

    ![Upload CSV](screenshots/upload.png)

2. **View the first few rows of the uploaded data:**

    ![Data Preview](screenshots/data_preview.png)

3. **View summary statistics and generated plots:**

    ![Statistics and Plots](screenshots/stats_plots.png)

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
