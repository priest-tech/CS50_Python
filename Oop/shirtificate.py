from fpdf import FPDF
def main():
    name = input("Name: ")
    shirtificate(name)


def shirtificate(name):
    pdf = FPDF()
    pdf.add_page('P', (210, 297)) # A4 size, potrait mode 
    pdf.set_font("Helvetica", size = 15)
    #title
    pdf.set_xy(0,15) #setting the title position
    pdf.set_font("Helvetica",'B', size = 20)
    pdf.cell(210,10, text="CS50 Shirtficate", align="C")   

    #Shirt image
    pdf.image("shirtificate.png", x=50, y=50, w=110)
    # name
    pdf.set_text_color(255,255, 255)  # blue text color
    pdf.set_xy(0, 95)  # Setting the position for the name
    pdf.set_font("Helvetica", 'B', 18)
    pdf.cell(210, 10, text=name, align="C")
   

    pdf.output("shirtificate.pdf")    




if __name__ == "__main__":
    main()    