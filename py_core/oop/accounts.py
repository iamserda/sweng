class BaseUser:
    def __init__(self, first: str, last: str, email: str, birthday=None):
        self.first = first
        self.last = last
        self.email = email
        self.birthday = birthday
        self.password = ""
        self.logon = False

    def set_password(self, password: str):
        self.password = password

    def login(self, password: str) -> dict:
        if self.password == password:
            self.logon = True
            return {"message": "Login successful!"}
        return {"message": "Failed to login!"}

    def logout(self) -> dict:
        if self.logon:
            self.logon = not self.logon
            return {"message": "Logout successful"}
        return {"message": "Guest cannot use logout feature!"}


class Admin(BaseUser):
    def __init__(self, first, last, email):
        super().__init__(first, last, email)
        self.permissions = []
        self.active = True

    def set_permissions(self, perms: list) -> None:
        self.permissions.append(*perms)

    def activate_mods(self, mod_obj) -> None:
        if isinstance(mod_obj, Moderator):
            mod_obj.mode_active = True
            print(mod_obj.get_mod_status())

    def deactivate_mods(self, mod_obj) -> None:
        if isinstance(mod_obj, Moderator):
            mod_obj.mode_active = False

    def is_active(self):
        return self.active


class Moderator(BaseUser):
    def __init__(self, f, l, e):
        super().__init__(f, l, e)
        self.managed_groups = []
        self.mod_active = False

    def get_mod_status(self) -> None:
        return self.mod_active


ducky = BaseUser("Doctor", "Mallard", "ducky@ncis.gov")
mozart_the_admin = Admin("Amadeus", "Mozart", "moz@myapp.com")
bach_the_moderator = Moderator("Joan Sebastian", "Bach", "jsbach@myapp.com")

mozart_the_admin.set_password("Mozart123")
bach_the_moderator.set_password("Bach123")
ducky.set_password("ducky123")

print(f"{mozart_the_admin.first} is an admin: {isinstance(mozart_the_admin, Admin)}")
print(
    f"{bach_the_moderator.first} is a Moderator: {isinstance(bach_the_moderator, Moderator)}"
)
print(f"{ducky.first} is a User: {isinstance(ducky, BaseUser)}")

print(
    f"Bach Account Status is: {'ACTIVE' if bach_the_moderator.get_mod_status() else 'INACTIVE'}"
)
mozart_the_admin.activate_mods(bach_the_moderator)
print(
    f"Bach Account Status is: {'ACTIVE' if bach_the_moderator.get_mod_status() else 'INACTIVE'}"
)
