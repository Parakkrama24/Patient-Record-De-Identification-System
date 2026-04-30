import re

PHONE_PATTERN = re.compile(r'\b0\d{9}\b')
EMAIL_PATTERN = re.compile(r'\b[\w\.-]+@[\w\.-]+\.\w+\b')

# Simple name heuristic (temporary)
NAME_PATTERN = re.compile(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b')