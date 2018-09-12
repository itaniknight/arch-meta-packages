import datetime
import os
import re
import shutil
import urllib.request

date = datetime.datetime.today().strftime("%Y.%m.%d")

##  functions

def read_html(target):
    data = urllib.request.urlopen(target)
    text = data.read()
    data.close()
    return text.decode("utf8")

##  get group list

group_html = read_html("https://archlinux.org/groups/")
group_list = re.findall(r"\/x86_64\/(.*?)\/", group_html)

##  set up directories

if os.path.exists("packages"):
    shutil.rmtree("packages")
os.mkdir("packages")

for item in group_list:
    os.mkdir("packages/@" + item)

##  main package iteration

total = len(group_list)
i = 0

for item in group_list:

    i += 1

    print(f"({i} / {total}) {item}")

    ##  create package lists

    item_html = read_html("https://archlinux.org/groups/x86_64/" + item)
    path = "package-lists/" + item
    item_list = re.findall(r"\/packages\/.*?\/x86_64\/(.*?)\/", item_html)

    ## create PKGBUILD

    pkgbuild = f'''# maintainer:  me <itaniknight@gmail.com>
# contributor: me <itaniknight@gmail.com>

pkgname="@{item}"
pkgdesc="Meta-package for group {item}."

pkgver={date}
pkgrel=1

url="https://archlinux.org/"

arch=("x86_64")
license=("MIT")

depends=(
'''

    for package in item_list:
        pkgbuild += "    " + package + "\n"

    pkgbuild += ")\n"

    ##  write PKGBUILD

    file = open("packages/@" + item + "/PKGBUILD", "w")
    file.write(pkgbuild)
    file.close()
