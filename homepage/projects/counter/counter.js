document.getElementById("decrease").addEventListener("click", function(){
    document.getElementById("value").innerHTML--;
});

document.getElementById("reset").addEventListener("click", function(){
    document.getElementById("value").innerHTML = 0;
});

document.getElementById("increase").addEventListener("click", function(){
    document.getElementById("value").innerHTML++;
});