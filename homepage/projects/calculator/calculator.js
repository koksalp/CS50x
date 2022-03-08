var nums = ["num0", "num1", "num2", "num3", "num4", "num5", "num6", "num7", "num8", "num9"];
for (let i=0; i<nums.length; i++){
    document.getElementById(nums[i]).addEventListener("click", function(){
        result = parseInt(result + this.innerHTML);
        document.querySelector(".result").innerHTML = result;
    });
}
var result = parseInt(document.querySelector(".result").innerHTML);
var temp_result = 0;


/*document.getElementById("addition").addEventListener("click", function(){
    this.style.backgroundColor = "green";
    temp_result = parseInt(result,10);
    result = 0;
    document.getElementById("equal").addEventListener("click", function(){
        result+=temp_result;
        document.querySelector(".result").innerHTML = result;
        temp_result = 0;
        document.getElementById("addition").style.backgroundColor = "#aaccff";
        document.getElementById("para1").innerHTML = "temp_result: " + temp_result + "result: " + result;
    });
});*/

var operations = ["addition", "substraction", "multiplication", "division"];
for (let i=0; i<operations.length; i++)
{
        document.getElementById(operations[i]).addEventListener("click", function(){
        this.style.backgroundColor = "green";
        temp_result = result;
        result = 0;

    });
}


document.getElementById("equal").addEventListener("click", function(){
    if (document.getElementById("substraction").style.backgroundColor == "green")
    {
        result = temp_result - result;
        document.getElementById("substraction").style.backgroundColor = "#aaccff";
    }
    else if (document.getElementById("multiplication").style.backgroundColor == "green")
    {
        result = temp_result * result;
        document.getElementById("multiplication").style.backgroundColor = "#aaccff";
    }
    else if (document.getElementById("division").style.backgroundColor == "green")
    {
        result = temp_result / result;
        document.getElementById("division").style.backgroundColor = "#aaccff";
    }
    else if (document.getElementById("addition").style.backgroundColor == "green")
    {
        result += temp_result;
        document.getElementById("addition").style.backgroundColor = "#aaccff";
    }
    document.querySelector(".result").innerHTML = result;

});
var result = parseInt(document.querySelector(".result").innerHTML);

document.getElementById("square").addEventListener("click", function(){
    result = Math.pow(result, 2);
    document.querySelector(".result").innerHTML = result;
});

document.getElementById("square_root").addEventListener("click", function(){
    result = Math.sqrt(result);
    document.querySelector(".result").innerHTML = result;
});
document.getElementById("clear").addEventListener("click", function(){
    result = 0
    document.querySelector(".result").innerHTML = result;
});





