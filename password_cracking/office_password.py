#Open 3 files that have passwords: docx, xlxs, pptx
import msoffcrypto,sys

filename=sys.argv[1].rsplit('.',1)[0] #rsplit is reverse split ,1 splits once only!
filetype=sys.argv[1].rsplit('.',1)[1]

office_types=["docx","pptx","xlsx"]

if filetype in office_types:
    #decrypted = io.BytesIO()
    with open(sys.argv[1], "rb") as f:
        try:
            file = msoffcrypto.OfficeFile(f)
            file.load_key(password=sys.argv[2],verify_password=True)  # Use password                   
            #file.decrypt(decrypted)               
            print("File Opened successfully")
        except:
            print("Incorrect Password")
else:
    print("Not a office file")