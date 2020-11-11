thisdict = {
    10: "ten",
    11: "eleven"
}

try:
    print(thisdict)
except NameError:
    print("error")
except:
    print("Other error")
else:
    print("No error")
finally:
    print("we done")

