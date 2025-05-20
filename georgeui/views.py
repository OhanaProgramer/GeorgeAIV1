# georgeui/views.py

from django.shortcuts import render
from datetime import datetime
import csv
from pathlib import Path

def home(request):
    today = datetime.today().strftime("%A, %B %d, %Y")
    context = {
        "username": "Jacque",
        "today": today,
        "focus": "UI-first assistant",
    }

    csv_path = Path(__file__).resolve().parent.parent / "task" / "masterList.csv"
    task_list = []
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            task_list = [row for row in reader if row["Project"] == "GeorgeAI1.0"]
    except Exception as e:
        task_list = [{"Seq": "!", "Project": "Error", "Task": str(e)}]

    context["tasks"] = task_list
    return render(request, "georgeui/home.html", context)