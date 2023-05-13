from configparser import ConfigParser

configur = ConfigParser()

ListOfLangs = "en", "fr"

print(f"""
(list)
    {ListOfLangs}
""")
lang = str(input("Please choose a language from (List): "))

language = "./Languages/"+lang
a = configur.read(language+".ini")

def L(what):
    return configur.get("lang", what)