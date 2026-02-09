def print_table(headers, rows):
    cols = len(headers)

    widths = [
        max(len(str(headers[i])), max(len(str(row[i])) for row in rows))
        for i in range(cols)
    
    ]
    def line():
        print("+" + "+".join("-" * (w + 2) for w in widths) + "+")

    def row_print(row):
        print("| " + " | ".join(str(row[i]).ljust(widths[i])for i in range(cols)) + " |")

    line()
    row_print(headers)
    line()

    for r in rows:
        row_print(r)
    
    line()

headers = ["Name", "Age", "Job"]

rows = [
    ["Murilo", 18, "MLOps"],
    ["Ana", 25, "Dev"],
    ["Jonh", 35, "Data Scientist"]
]

print_table(headers, rows)