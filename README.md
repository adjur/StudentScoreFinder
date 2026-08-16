# StudentScoreFinder

StudentScoreFinder is a Python tool that extracts structured student assessment data from school-generated PDF reports and prepares it for easier review and teacher-specific analysis.

The project was created to reduce the amount of manual searching required when working with large assessment reports and to make relevant student information easier to organize and compare.

## What It Does

StudentScoreFinder processes PDF assessment reports and extracts useful student-level data such as:

* Student name
* Student number
* Booklet ID
* Assessment score

The tool identifies relevant sections of a PDF, parses the information, and converts the results into structured data that can be used for further analysis.

## Why I Built It

School assessment reports can contain large amounts of information that teachers may need to search through manually.

This project explores how Python can automate that process by turning semi-structured PDF reports into usable data.

The goal is to make assessment information faster to locate, easier to organize, and more practical for classroom use.

## Technologies

* Python
* `pdfplumber`
* PDF parsing
* Data extraction
* Structured data processing
* CSV-ready data

## Project Structure

```text
StudentScoreFinder/
│
├── src/
│   └── application source files
│
├── .gitignore
├── README.md
├── requirements.txt
└── test_pdf.py
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/StudentScoreFinder.git
cd StudentScoreFinder
```

Create and activate a virtual environment if desired:

```bash
python -m venv .venv
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Then run the application or test script using your local PDF files.

## Privacy

Student assessment reports may contain personally identifiable or protected educational information.

For privacy and security:

* Real student reports are not included in this repository.
* Sample or test data should be anonymized.
* Sensitive PDFs and generated student data should remain excluded from Git through `.gitignore`.
* The repository should never contain real student names, identification numbers, or protected assessment records.

## Current Development

The current version focuses on extracting structured assessment information from PDF reports.

Future development may include:

* Comparing extracted results against a class roster
* Exporting results directly to CSV
* Improved handling of different report formats
* More flexible score and section detection
* A simple interface for nontechnical users

## Skills Demonstrated

This project demonstrates experience with:

* Python development
* File and document processing
* Parsing semi-structured data
* Data cleaning and organization
* Automation
* Privacy-aware software development
* Designing software around a real-world workflow

## About

StudentScoreFinder began as a practical solution to a repetitive data-review problem. It is an example of how relatively small automation tools can make existing workflows faster and easier to manage.
