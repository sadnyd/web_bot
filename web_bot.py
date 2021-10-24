while 1>0:
    try:
            import pyautogui as p
            import pytesseract as pt
            import time
            import xlrd
            

            class Test:
             
                def imgrecog(self):
                    x=50
                    lt=""
                    while lt!=35:
                        img = p.screenshot(".\img.png",region=(1380,890,x,30))
                        text=pt.image_to_string("img.png").lstrip()
                        x+=25
                        lt=ord(text[-3])
                        text=text[:-3].strip()
                        print(text)
                        print("l ",lt," l")
                    return text
                        

                def tcheck(self,text):
                    texto='this sentence is not there in the check, want me to add?'
                    textc=""
                    text= text.lower()
                    # print(text)
                    # time.sleep(0.5)
                    wb=xlrd.open_workbook(".\excel.xls")
                    sheet= wb.sheet_by_index(0)
                    n=sheet.nrows
                    print(n)
                    # time.sleep(2)
                    for i in range(n):
                        textc=str(sheet.cell_value(i,0)).lower().strip(" ")
                        print(textc)
                        # time.sleep(2)
                        if text==textc:
                            texto=str(sheet.cell_value(i,1)).lower()
                            break
                    print("\n",texto,"    output")
                    # time.sleep(2)
                    return texto



            t1= Test()
            time.sleep(0.2)
            t1.tcheck(t1.imgrecog())
           
    except:
        print("error")
