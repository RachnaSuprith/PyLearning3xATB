def allowed_to_enter_class(name, password):
    if name == "Rachna":
        if password == "yes":
            print("allowed")
        else:
            print("not allowed")


allowed_to_enter_class("Rachna", "YES")
