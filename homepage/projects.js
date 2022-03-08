var p = document.querySelectorAll("p");
var button = document.querySelectorAll(".button");
var projects = ["projects/calculator/calculator.html", "projects/counter/counter.html", "projects/grocery bud/grocery bud.html"];
for(let i = 0; i < button.length; i++)
{
    button[i].addEventListener("click", function(){
        if (p[i+1].innerHTML.length != 0)
        {
            p[i+1].innerHTML = "";
        }
        else
        {
            p[i + 1].innerHTML = "This is project number " + (i + 1) + " and you can visit this project by clicking ";
            var project_link = document.createElement("a");
            var project = projects[i];
            project_link.href = project;
            project_link.target = "_blank";
            project_link.innerText = "here";
            project_link.title = project.slice(project.indexOf("/") + 1, project.lastIndexOf("/"));
            p[i + 1].appendChild(project_link);
            for(let j = 1; j <= button.length; j++)
            {
                if ((i + 1) != j)
                    p[j].innerHTML = "";
            }
        }
    });
}