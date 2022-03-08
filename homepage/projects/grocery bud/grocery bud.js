var main_div = document.getElementById("main-div");

var submit = main_div.querySelector(".submit");
var input = main_div.querySelector(".input");
var p = document.getElementById("para1");
var clear = 0;
var edit;
function empty()
{
    p.style = "color: black; background-color: rgba(255, 0, 0, 0.5); font-weight: bold;";
    p.innerHTML = "Enter a value";
}
function add()
{
    p.style = "color: black; background-color: rgba(0, 255, 0, 0.5); font-weight: bold;";
    p.innerHTML = "Item Added To The List";
}
function p_default()
{
    p.style = "color: white; background-color: white;";
}
submit.addEventListener("click", function(){
    if(submit.innerHTML == "Submit")
    {
        if (input.value == "" || input.value.trim() == "")
        {
            empty();
        }
        else
        {
            if (clear == 0)
            {
                var clear_div = document.createElement("DIV");
                clear_div.classList.add("clear");
                clear_div.innerHTML = "Clear All";
                main_div.appendChild(clear_div);
                clear = 1;
                clear_div.addEventListener("click", function(){
                    var list_div = main_div.querySelectorAll(".items");
                    for (let i=0; i<list_div.length; i++){
                        list_div[i].remove();
                    }
                    clear_div.remove();
                    clear=0;
                });
            }
            var new_div = document.createElement("DIV");
            new_div.classList.add("items");
            new_div.innerHTML = input.value;
            var edit_icon = document.createElement("SPAN");
            edit_icon.className = "fa fa-edit edit";
            new_div.appendChild(edit_icon);
            var trash_icon = document.createElement("SPAN");
            trash_icon.className = "fa fa-trash-o trash";
            new_div.appendChild(trash_icon);
            trash_icon.addEventListener("click", function(){
                new_div.remove();
                if (main_div.querySelectorAll(".items").length == 0)
                {
                    main_div.querySelector(".clear").remove();
                    clear = 0;
                }
            });
            edit_icon.addEventListener("click", function(){
                submit.innerHTML = "Edit";
                input.value = new_div.innerText;
                edit = new_div;
            });
            main_div.insertBefore(new_div, main_div.querySelector(".clear"));
            add();
        }
        setTimeout(p_default, 1000);
        input.value = "";
    }
    else
    {
        edit.innerText = input.value;
        submit.innerHTML = "Submit";
        input.value = "";
    }
});