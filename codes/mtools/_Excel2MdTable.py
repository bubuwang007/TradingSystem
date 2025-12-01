import openpyxl as op


class Excel2MdTable:

    def __init__(
        self, excel_file: str, title, sheet_name: str = None, type: str = "vuepress"
    ):
        self.wb = op.load_workbook(excel_file)
        self.sheet = self.wb[sheet_name] if sheet_name else self.wb.active
        self.type = type
        self.title = title

    def generate(self) -> str:
        md_table = []
        for row in self.sheet.iter_rows():
            md_row = (
                "| "
                + " | ".join(
                    self.cell2md(cell) for cell in row if str(cell.value) != "None"
                )
                + " |"
            )
            md_table.append(md_row)

        if md_table:
            header_cells = md_table[0].count("|") - 1
            separator = "| " + " | ".join(["---"] * header_cells) + " |"
            md_table.insert(1, separator)

        if self.type == "vuepress":
            start = f'::: table title="{self.title}"'
            end = ":::"
            md_table.insert(0, start)
            md_table.append(end)
        return "\n".join(md_table)

    def cell2md(self, cell) -> str:
        color = cell.font.color
        if color.type == "rgb":
            return f'<font color="#{color.rgb[2:]}">{cell.value}</font>'
        return str(cell.value)

    def to_file(self, output_file: str):
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(self.generate())
