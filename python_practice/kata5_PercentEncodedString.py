def url_encode(text):
    encoding = ""
    for i in text:
        if i == " " and text[0] != " ":
            encoding += "%20"
        else:
            encoding += i
    return encoding



print(url_encode("Lighthouse Labs"))
print(url_encode(" Lighthouse Labs  "))
print(url_encode("blue is greener than purple for sure"))
