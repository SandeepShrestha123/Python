"""
This is the example of understanding merging dictionary
"""

dic1 = {
    "Sandeeep": "Paknajol",
    "Srestaa": "Ason",
    "Anuj": "Chhetrapati"
}

dic2 = {
    "Sandeep": 9844373045,
    "Srestaa": 9841524379
}

merged = dic1 | dic2

for name, values in merged.items():
    print(f"{name} = {values}")
