var all_h2 = document.querySelectorAll(".div > h2");
var all_text = document.querySelectorAll(".text");
var arrows = document.querySelectorAll(".arrow");

var countries = [
    "Turkey",
    "United States of America",
    "Portugal",
    "Spain",
    "Italy",
    "France",
    "Germany",
    "Hungary",
    "Romania",
    "Belgium",
    "Netherlands",
    "Greece"
    ];

var ol = document.createElement("ol");
for (let i = 0; i < countries.length; i++)
{
    var li = document.createElement("li");
    var li_text = document.createTextNode(countries[i]);
    li.appendChild(li_text);
    ol.appendChild(li);
    ol.appendChild(document.createElement("br"));
}

all_text[2].appendChild(ol);

for (let i = 0; i < all_h2.length; i++)
{
    all_h2[i].addEventListener("click", function(){

        if (arrows[i].classList[1] ==  "up")
        {
            arrows[i].classList.remove("up");
            arrows[i].classList.add("down");
            all_text[i].style.display = "block";
        }
        else
        {
            arrows[i].classList.remove("down");
            arrows[i].classList.add("up");
            all_text[i].style.display = "none";
        }
    });
}