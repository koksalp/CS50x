var logos = document.querySelectorAll(".logo");
var para1 = document.getElementById("para1");

for (let i=1; i<logos.length; i++)
{
    logos[i].addEventListener("click", function(){
        para1.innerHTML = "linkedin only";
        setTimeout(function(){ para1.innerHTML = ""; }, 500);
    });
}
