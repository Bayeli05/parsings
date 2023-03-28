import requests
import img2pdf


def get_data():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44"
    }

    img_list = []
    for i in range(1, 49):
        url =f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"media/{i}.jpg")
            print(f"Download {i} of 48")

    print("#" * 20)    
    print(img_list)    

    # create PDF file

    with open("result.pdf", "wb")as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file created successfully")


def write_to_pdf():
    # print(os.listdir("media"))
    img_list = [f"media/{i}.jpg"  for i in range(1, 49)]
    
    with open("result.pdf", "wb")as f:
        f.write(img2pdf.convert(img_list))

    print("PDF file created successfully")

def main():
    # get_data()
    write_to_pdf()

if __name__ == "__main__":
    main()