while 1>0:
    try:
            import pyautogui as p
            import pytesseract as pt
            import time
            

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
               


            t1= Test()
            t1.imgrecog()
            time.sleep(0.2)
         
    except:
        print("error")
