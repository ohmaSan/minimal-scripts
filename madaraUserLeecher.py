import requests
from bs4 import BeautifulSoup

print(" \n ==>MadaraUserLeecher v1.4<==")

# headers
headers_param = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}

# welcome and input
print("\nSample URL: http://target.com/a/b/{}")
target = input("Target: ")
print("\n")

if "{}" not in target:
    print("Sample URL: http://target.com/a/b/{} \n"
          "Exiting!")
else:
    first_page = int(input("First Page: "))
    last_page = int(input("Last Page: "))
    increase = int(input("Increase: "))

    # html tags
    first_html = input("First HTML Tag: ")
    second_html = input("Second HTML Tag: ")
    third_html = input("Third HTML Tag: ")
    print("\nUsers are leeching! Please wait...")

    # get_istegi ve respoense
    for i in range(first_page, last_page, increase):
        get_request = requests.get(target.format(i), headers=headers_param)

        # content
        full_content = get_request.content

        # bs parse etme
        soup = BeautifulSoup(full_content, "html.parser")

        # select between html tags
        users = soup.find_all(first_html, {second_html: third_html})

        # clear user list
        with open("user_list.txt", "a") as f:
            for user in users:
                f.write(str(user.text) + "\n")
    user_count = sum(1 for line in open('user_list.txt'))
    print("\nProcess is finished!\n"
          f"User count: {user_count}")
