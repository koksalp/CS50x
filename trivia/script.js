//function used for default color
function color_remain_same(x)
{
    for (let i=0; i<x.length; i++)
    {
    x[i].style = "background-color: #aaccff; color: black;"
    }
}
var div_elements= document.getElementById("first_div").querySelectorAll("div.question_div");
//if correct answer gets clicked
document.getElementById("correct1").addEventListener("click", function(){

    color_remain_same(div_elements);
    this.style = "background-color: green; color: white;"
    document.getElementById("para1").innerHTML = "CORRECT!";
    });
//function1 is called when one of the wrong answers get clicked
function function1(element)
{   color_remain_same(div_elements);
    document.getElementById("para1").innerHTML = "FALSE!";
    element.style = "background-color: red; color: white;";
}
//checks answers for second question
document.getElementById("check_answer").addEventListener("click", function(){
    var answer = document.getElementById("input").value;
    if (answer == "Switzerland" || answer == "switzerland")
    {
    document.getElementById("para2").innerHTML = "CORRECT!";
    this.style = "background-color: green; color: white;"
    }
    else
    {
        document.getElementById("para2").innerHTML = "FALSE!";
        this.style = "background-color: red; color: white;"
    }
});

//checks how many correct answers user have
document.getElementById("finish_test").addEventListener("click", function(){
    if ((document.getElementById("input").value == "Switzerland" || document.getElementById("input").value == "switzerland") && document.getElementById("para1").innerHTML == "CORRECT!")
    {
        document.getElementById("para3").innerHTML = "You have 2 correct answers<br/>CONGRATULATIONS!";
    }
    else if (document.getElementById("input").value == "Switzerland" || document.getElementById("input").value == "switzerland" || document.getElementById("para1").innerHTML == "CORRECT!")
    {
        document.getElementById("para3").innerHTML = "You have 1 correct answers<br/>CONGRATULATIONS!";
    }
    else
    {
        document.getElementById("para3").innerHTML = "You have no correct answers. Try again.";
    }
});