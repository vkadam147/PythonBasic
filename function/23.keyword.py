def wish(name,city):
    print(f"Name:{name} city:{city}")

wish("vaishnavi","pune")# both positional ------>valid

wish(city="Pune",name="Vaishnavi")#both keyword ----->valid

wish("Vaishnavi",city="Pune")# first is positional and second is keyword ----->valid

# wish(name="Vaishnavi","Pune");# first keyword and second is positional ----->Invalid

# wish("pune",name="vaishnavi");

