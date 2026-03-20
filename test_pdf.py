import pdfplumber # PDF library to extract text from pdf files
import re # Regular expressions library for pattern matching

print("Script started")

pdf_path = "data/input/Nur125.pdf" # Path to the pdf file to be processed

def is_student_row(line):
    if not line:
        return False

    line = line.strip()

import re

import re

def is_student_row(line):
    if not line:
        return False

    line = line.strip()

    has_name = re.match(r"^[A-Za-z'`\- ]+,\s+[A-Za-z'`\- ]+", line)
    has_percent = re.search(r"\d{1,3}\.\d%", line)
    has_score_ending = re.search(r"\s\d+\s+(N/A|\d+)\s+\d+$", line)

    return bool(has_name and has_percent and has_score_ending)


def is_student_page(text):
    if not text:
        return False

    lines = text.split("\n")
    student_like_count = 0

    for line in lines:
        if is_student_row(line):
            student_like_count += 1

    return student_like_count >= 3

def parse_student_row(line):
    parts = line.split()

    name = parts[0] + " " + parts[1]
    remaining = parts[2:]

    points_possible = remaining[-1]
    adjusted_points = remaining[-2]
    original_points = remaining[-3]
    score_percent = remaining[-4]

    ids = remaining[:-4]

    student_number = None
    booklet_id = None

    if len(ids) == 2:
        student_number = ids[0]
        booklet_id = ids[1]
    elif len(ids) == 1:
        booklet_id = ids[0]

    return {
        "name": name,
        "student_number": student_number,
        "booklet_id": booklet_id,
        "score_percent": score_percent,
        "original_points": original_points,
        "adjusted_points": adjusted_points,
        "points_possible": points_possible,
    }

def extract_scores_from_pdf(pdf_path):
    results = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            if not is_student_page(text):
                print(f"Skipping page {i + 1} as it does not contain student information.")
                continue

            print(f"\nProcessing page {i + 1}...")

            lines = text.split("\n")

            for line in lines:
                if is_student_row(line):
                    
                    parsed = parse_student_row(line)
                    print(parsed)
                    results.append(parsed)

    return results


rows = extract_scores_from_pdf(pdf_path)

print(f"\nTotal student-like rows found: {len(rows)}")