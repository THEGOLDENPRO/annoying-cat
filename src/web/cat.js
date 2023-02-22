class Cat {
    constructor(cat_dict) {
        this.name = cat_dict["name"];
        this.gender = cat_dict["gender"]
    }

    talk(text, rm_delay) {
        return pywebview.api.talk(text, rm_delay);
    }
}

