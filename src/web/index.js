var cat_name = document.getElementById("cat_name");

window.addEventListener('pywebviewready', function() {

    pywebview.api.get_cat().then(

        function(dict) {
            var cat = new Cat(dict);

            console.log("Getting cat --> ", dict);

            cat_name.innerText = cat.name;
        }

    )

})