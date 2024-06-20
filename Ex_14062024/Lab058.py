def allowed_to_enter_class(name):
    match name:
        case "Raksha":
            print("Allowed")
        case "Vaishnavi":
            print("Allowed")
        case_:
            print("not allowed")

    allowed_to_enter_class("Vaishnavi")
