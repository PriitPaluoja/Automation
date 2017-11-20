from bs4 import BeautifulSoup
from collections import defaultdict

# From EDU page download as HTML (Klass(id) with order of:
# Õppeaine
# Õpetaja
# Ruum
# Klass(id)
# Kellaaeg


with open("classes.html", "r", encoding="UTF-8") as f:
    soup = BeautifulSoup(f.read().replace("<br/>", "*")
                         .replace("8:00", "08:00")
                         .replace("8:55", "08:55")
                         .replace("9:50", "09:50"),
                         'html.parser')


# Remove unnecessary tags:
def clean(soup, whitelist=tuple()):
    for tag in soup.findAll(True):
        for attr in [attr for attr in tag.attrs if attr not in whitelist]:
            del tag[attr]
    return soup


# classes -> days : time : list ( ained  )
classes = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))

for tr in soup.find_all('tr'):
    for day, td in enumerate(tr.find_all("td", {"class": "xl2"})):
        del td["class"]

        str_value = clean(td, ()).string
        # Could be day or not. Days are "Es, Te..."
        if day == 0 and len(str_value.strip()) == 2:
            current_day = str_value.strip()
        else:
            # In this case contains values
            splt = str_value.strip().split("*")
            if len(splt) == 5:
                course, teacher, room, class_, time = splt[0], splt[1], splt[2], splt[3], splt[4]
                for c in class_.split(","):
                    if "_" in c or "-" in c:
                        continue
                    classes[c][time][current_day].add(course + " - " + room)
            else:
                pass

days = ["Es", "Te", "Ko", "Ne", "Re"]

# Create output
out = ""
for class_ in sorted(classes.keys()):
    out += class_ + "\n\t" + "\t".join(days) + "\n"
    for time in sorted(classes[class_].keys()):
        out += time + "\t"
        for day in days:
            out += str(sorted(list(classes[class_][time][day]))) + "\t"
        out += "\n"

out = out.replace("[", "").replace("]", "").replace("'", "")

out = out \
    .replace("Es", "Esmaspäev") \
    .replace("Te", "Teisipäev") \
    .replace("Ko", "Kolmapäev") \
    .replace("Ne", "Neljapäev") \
    .replace("Re", "Reede")

out = out \
    .replace("Mat", "Matemaatika") \
    .replace("Kk", "Kehaline") \
    .replace("Muus", "Muusika") \
    .replace("Tööõp", "Tööõpetus") \
    .replace("Kirj", "Kirjandus") \
    .replace("Ajal", "Ajalugu") \
    .replace("Bio", "Bioloogia") \
    .replace("Füüs", "Füüsika") \
    .replace("Ik", "Inglise keel") \
    .replace("Vk", "Vene keel") \
    .replace("Geo", "Geograafia") \
    .replace("Sk", "Saksa keel") \
    .replace("Ek", "Eesti keel")

with open("timetable.txt", "w", encoding="UTF-8") as f:
    f.write(out)
