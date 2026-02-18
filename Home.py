from flask import Flask, render_template, request, redirect, url_for, session, send_file
import pandas as pd
import os
import uuid
from services.visualization import create_chart
from services.export import export_pdf, export_word, export_jpeg
from services.data_cleaning import clean_data
import plotly.io as pio

app = Flask(__name__)
app.secret_key = os.environ.get("DATUM_SECRET_KEY", "datum_dev_key")
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["EXPORT_FOLDER"] = "exports"

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["EXPORT_FOLDER"], exist_ok=True)

ALLOWED_EXTENSIONS = {"csv"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return render_template("upload.html", error="No file selected")
        if not allowed_file(file.filename):
            return render_template("upload.html", error="Only CSV files are supported")
        try:
            df = pd.read_csv(file)
        except Exception as e:
            return render_template("upload.html", error=f"Failed to read CSV: {str(e)}")

        df = clean_data(df)

        data_filename = f"cleaned_{uuid.uuid4().hex}.csv"
        data_path = os.path.join(app.config["UPLOAD_FOLDER"], data_filename)
        df.to_csv(data_path, index=False)

        session["data_path"] = data_path

        summary = {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "column_names": df.columns.tolist()
        }

        sample_html = df.head(10).to_html(index=False)
        return render_template("upload.html", summary=summary, uploaded=True, sample_html=sample_html)

    return render_template("upload.html")


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    data_path = session.get("data_path")
    if not data_path or not os.path.exists(data_path):
        return redirect(url_for("upload"))

    df = pd.read_csv(data_path)
    columns = df.columns.tolist()
    graph_html = None

    if request.method == "POST":
        chart_type = request.form.get("chart_type")
        x_column = request.form.get("x_column")
        y_column = request.form.get("y_column")

        if not x_column or x_column not in columns:
            return render_template("dashboard.html", columns=columns, graph_html=None, error="Select a valid X column")
        if chart_type != "Histogram" and (not y_column or y_column not in columns):
            return render_template("dashboard.html", columns=columns, graph_html=None, error="Select a valid Y column")

        fig = create_chart(df, chart_type, x_column, y_column)

        last_chart_filename = f"chart_{uuid.uuid4().hex}.json"
        last_chart_path = os.path.join(app.config["EXPORT_FOLDER"], last_chart_filename)
        with open(last_chart_path, "w", encoding="utf-8") as f:
            f.write(fig.to_json())
        session["last_chart_path"] = last_chart_path

        graph_html = fig.to_html(full_html=False)

    return render_template("dashboard.html",
                           columns=columns,
                           graph_html=graph_html)


@app.route('/export/<filetype>')
def export(filetype):
    last_chart_path = session.get("last_chart_path")
    if not last_chart_path or not os.path.exists(last_chart_path):
        return redirect(url_for("dashboard"))

    with open(last_chart_path, "r", encoding="utf-8") as f:
        fig_json = f.read()
    fig = pio.from_json(fig_json)

    if filetype == "pdf":
        path = export_pdf(fig)
    elif filetype == "word":
        path = export_word(fig)
    elif filetype == "jpeg":
        path = export_jpeg(fig)
    else:
        return redirect(url_for("dashboard"))

    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
