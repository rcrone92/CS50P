# import necessary libraries
from fpdf import FPDF
# define global variables

class PDF(FPDF):
    def wording(self):
        self.image("./shirtificate.png", 15, 75, 195)
        self.set_font("Times", "B", 36)
        self.cell(0, 55, "CS50 Shirtificate", align="C")
        self.ln(20)



def main():
    name = input("Name: ")
    create(name)


def create(name):
    pdf = PDF()
    pdf.add_page(orientation="P", format="a4")
    pdf.set_font("Times", "B", 12)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
