from fnmatch import fnmatch


class Email:
    def __init__(self, mail):
        self.original_mail = mail
        self.short_mail = mail

    @property
    def short_mail(self):
        return self.__mail

    @short_mail.setter
    def short_mail(self, value):
        if not fnmatch(value, "*@*.*"):
            raise ValueError("Хуёвый email")
        if value.split("@")[-1] == "googlemail.com":
            value = value.split("@")[0] + "@" + "gmail.com"
        if "gmail" in value:
            value = value.split("@")[0].replace(".", "") + "@" + value.split("@")[-1]
        value = value.split("@")[0].split("+")[0] + "@" + value.split("@")[-1]
        self.__mail = value


a = Email("a.b.c+test@googlemail.com")
print(a.original_mail, "\t\t", a.short_mail)