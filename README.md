# WD Preprocessing for IBMcloud

WD Preprocessing for IBMcloud is a Python package designed to authenticate and fetch project data from IBM Watson Discovery. It preprocesses the raw JSON data from Watson Discovery and reformats it into a structured format.

## Features

- Authenticate with IBM Watson Discovery
- Fetch and preprocess data from Watson Discovery projects
- Save data in a structured JSON format

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or above
- Pip for installing Python packages

### Installation

Clone the repository to your local machine:

Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the package in editable mode:
```bash
pip install -e .
```

### Configuration

Create a .env file in the root directory of the project and add your IBM Watson 

Discovery credentials:
```bash
API_KEY=your_ibm_watson_discovery_api_key
PROJECT_ID=your_project_id
```

### Usage

To use the package, run the main.py script:
```bash
python ./src/main.py
```
