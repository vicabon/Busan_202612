import os, sys, re, json
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

print("Starting full pipeline to generate Excel, AGENT.md, AGENT.html, SKILL.md, SKILL.html, README.md")
