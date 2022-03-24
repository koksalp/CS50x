// get all the elements 
const translate = document.getElementById("translate"); 
const input_text = document.getElementById("input_text"); 
const translated_text = document.getElementById("translated_text");   
const input_list = document.getElementById("input_list"); 
const output_list = document.getElementById("output_list"); 
const clear = document.getElementById("clear"); 
const change = document.getElementById("change");   
const default_button = document.querySelectorAll(".default"); 
const project_details = document.getElementById("project_details"); 

// function to generate language options 
function set_languages()
{
    // get default languages 
    const input_lang = localStorage.getItem("input_lang"); 
    const output_lang = localStorage.getItem("output_lang"); 
    
    // API call for all supported languages 
    fetch("https://translo.p.rapidapi.com/get_languages", {
        "method": "GET",
        "headers": {
            "x-rapidapi-host": "translo.p.rapidapi.com",
            "x-rapidapi-key": "37860be40amsh7dfdd14f8554a3ap1ff391jsnb274c13b59cc"
        }
    })
    .then(response => response.json())
    .then(data => {
        for (lang in data.codes) 
        {
            // generate language options for both dropdown lists 
            [input_list, output_list].forEach((list , index)=> { 

                // create an option element 
                const option = document.createElement("option"); 

                // language as written in english i.e. german 
                option.innerHTML = data.codes[lang]; 

                // language code i.e. en for english 
                option.value = lang; 

                // show languages selected by default 
                if (index === 0) 
                {
                    if (data.codes[lang] === input_lang)
                    {
                        option.setAttribute('selected', true); 
                    }
                }
                else  
                {
                    if (data.codes[lang] === output_lang)
                    {
                        option.setAttribute('selected', true); 
                    }
                }
                list.appendChild(option); 
            })
        }
    })
    .catch(err => {
        console.error(err);
    });
}

// function call 
set_languages(); 

// translate process 
translate.addEventListener("click", () => {   

    // source language 
    const from = input_list.value; 

    // target language 
    const to = output_list.value; 

    // text to be translated 
    const text = input_text.value; 

    // API call for translation 
    fetch(`https://translo.p.rapidapi.com/translate?text=${text}&from=${from}&to=${to}&translations=false`, {
        "method": "GET",
        "headers": {
            "x-rapidapi-host": "translo.p.rapidapi.com",
            "x-rapidapi-key": "37860be40amsh7dfdd14f8554a3ap1ff391jsnb274c13b59cc"
        }
    })
    .then(response => response.json())
    .then(data => {

        // show translated text 
        translated_text.value = data.translated_text; 
    })
    .catch(err => {
        console.error(err);
    });
});

// clear both textareas 
clear.onclick = () => {
    input_text.value = ""; 
    translated_text.value = ""; 
}

// switch between languages 
change.onclick = () => { 

    // swap values 
    output_list.value = [input_list.value, input_list.value = output_list.value][0]; 
    translated_text.value = [input_text.value, input_text.value = translated_text.value][0];  
    
    // if translated text area is empty before swapping, clear input textarea also  
    if (input_text.value == "")
    {
        translated_text.value = ""; 
    }
}

// set default languages 
default_button.forEach((button, index) => { 
    button.onclick = () => { 

        // get selected language 
        const selected_lang = index === 0 ? input_list.options[input_list.selectedIndex].text : output_list.options[output_list.selectedIndex].text;  

        // decide the button pushed 
        const input_or_output = index === 0 ? "input_lang" : "output_lang"; 

        // use localstorage for storing default language 
        localStorage.setItem(input_or_output, selected_lang); 

        // create a JSON object for notification 
        const notification = {
            type: "basic",
            iconUrl: "icon48.png",
            title: "Success",
            message: `${selected_lang} is set as default language.` 
        }

        // create a notification using chrome API 
        chrome.notifications.create("", notification, function(id) { 
            
            // clear notification after 2 seconds 
            const timer = setTimeout(function(){chrome.notifications.clear(id);}, 6000); 
        }); 
    } 
})

// show project details    
project_details.onclick = () => {
    const details_notif = {
        type: "basic",
        iconUrl: "icon48.png",
        title: "Project Details",
        message: "CS50 Final Project: CS50 Translator\nCreated by: Alp Köksal\nİstanbul/Turkey"  
    } 
    chrome.notifications.create("detail", details_notif, function(id) { 
            
        // clear notification after 10 seconds 
        const detail_timer = setTimeout(function(){chrome.notifications.clear(id);}, 10000); 
    }); 
}