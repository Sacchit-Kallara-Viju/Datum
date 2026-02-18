# 📊 Datum

## Transform Data Into Insight

Datum is a modern SaaS-ready data analytics and visualization web
application built using **Python (Flask)** for the backend and
**HTML/CSS + Plotly.js** for the frontend.

It allows users to upload CSV files, automatically clean data, generate
interactive visualizations, and export reports in multiple formats (PDF,
JPEG, Word).

------------------------------------------------------------------------

## 🚀 Features

### ✅ Data Upload & Cleaning

-   Drag & Drop CSV Upload
-   Automatic duplicate removal
-   Missing value handling
-   Cleaned dataset summary
-   Column detection and metadata preview

### 📈 Interactive Visualization

-   Bar Chart
-   Line Chart
-   Scatter Plot
-   Histogram
-   Dynamic X/Y axis selection
-   Fully interactive Plotly charts (zoom, pan, hover)

### 🎨 Modern SaaS UI

-   Professional dashboard layout
-   Sidebar navigation
-   Dark / Light theme switcher (saved in localStorage)
-   Animated transitions
-   Split dashboard layout (Configuration + Chart View)
-   Progress stage indicator (Upload → Visualize → Export)

### 📤 Export Options

-   Export as PDF
-   Export as JPEG
-   Export as Word Document
-   High-resolution export using Kaleido

------------------------------------------------------------------------

## 🏗 Tech Stack

### Backend

-   Python 3.9+
-   Flask
-   Pandas
-   Plotly
-   Kaleido
-   python-docx
-   Gunicorn (for production deployment)

### Frontend

-   HTML5
-   CSS3 (Modern SaaS Styling)
-   JavaScript
-   Plotly.js

------------------------------------------------------------------------

## 📂 Project Structure

    Datum/
    │
    ├── Home.py
    ├── requirements.txt
    │
    ├── services/
    │   ├── __init__.py
    │   ├── data_cleaning.py
    │   ├── visualization.py
    │   └── export.py
    │
    ├── static/
    │   ├── css/
    │   │   └── styles.css
    │   └── js/
    │       └── main.js
    │
    └── templates/
        ├── base.html
        ├── index.html
        ├── upload.html
        └── dashboard.html

------------------------------------------------------------------------

## ⚙️ Installation

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/yourusername/datum.git
cd datum
```

### 2️⃣ Create Virtual Environment

``` bash
python -m venv venv
```

Activate:

Windows:

``` bash
venv\Scripts\activate
```

Mac/Linux:

``` bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Running the Application (Development)

``` bash
python Home.py
```

Open your browser:

    http://127.0.0.1:5000

------------------------------------------------------------------------

## 🚀 Production Deployment

Install Gunicorn:

``` bash
pip install gunicorn
```

Run:

``` bash
gunicorn Home:app
```

For cloud deployment (Render / Railway / Heroku): Set start command to:

    gunicorn Home:app

------------------------------------------------------------------------

## 📊 Application Workflow

1.  User uploads CSV file\
2.  Backend cleans dataset using Pandas\
3.  Columns are extracted dynamically\
4.  User selects chart type and axes\
5.  Plotly generates interactive visualization\
6.  Chart can be exported as PDF / JPEG / Word

------------------------------------------------------------------------

## 🔒 Security Considerations

-   Only CSV files are accepted
-   File uploads stored in controlled directory
-   Session-based chart storage
-   Production deployment recommended behind HTTPS

------------------------------------------------------------------------

## 🌙 Theme System

Datum includes a built-in theme switcher: - Dark Mode - Light Mode -
Preference saved via localStorage

------------------------------------------------------------------------

## 📌 Future Improvements

-   Authentication & user accounts
-   Cloud storage integration
-   Dashboard save/share functionality
-   Multi-chart layouts
-   Database integration
-   Advanced analytics (correlation, regression)
-   Role-based access control

------------------------------------------------------------------------

## 🧠 Use Cases

-   Data Science Projects
-   Business Intelligence
-   Academic Research
-   CSV Data Exploration
-   Startup Analytics Tools

------------------------------------------------------------------------

## 📄 License

This project is open-source and available under the MIT License.

------------------------------------------------------------------------

## 👨‍💻 Author

Built with Python, Flask & Plotly.
