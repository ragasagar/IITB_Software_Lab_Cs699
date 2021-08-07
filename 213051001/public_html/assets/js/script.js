var checkbar1 = document.getElementById("hobbie1");
var checkbar2 = document.getElementById("hobbie2");
var checkbar3 = document.getElementById("hobbie3");
var checkbar4 = document.getElementById("hobbie4");
var ischecked = false;
var button = document.getElementById("hobbie-button");

button.disabled = true;

function onClickCheckbox(){
    console.log(checkbar4.value);
    if(checkbar1.checked  || checkbar2.checked || checkbar3.checked || checkbar4.checked){
        button.disabled = false;
    }else{
        button.disabled = true;
    }

    if(!checkbar1.checked){
        document.getElementById(checkbar1.value).style.display ="none";
    }
    if(!checkbar2.checked){
        document.getElementById(checkbar2.value).style.display ="none";
    }
    if(!checkbar3.checked){
        document.getElementById(checkbar3.value).style.display ="none";
    }
    if(!checkbar4.checked){
        document.getElementById(checkbar4.value).style.display ="none";
    }
}

function onClickButton(){
    var modalbody = document.getElementById("hobbie-value");
    modalbody.innerHTML = '<p> Selected Hobbies:'+ (checkbar4.checked? checkbar4.value+" ": "") + 
    (checkbar3.checked? checkbar3.value+" " : "" )+
    (checkbar2.checked? checkbar2.value+" ": "")+
    (checkbar1.checked? checkbar1.value+"": "") + "</p>";
}

function onClickModalButton(){
    if(checkbar1.checked){
        document.getElementById(checkbar1.value).style.display ="flex";
    }
    if(checkbar2.checked){
        document.getElementById(checkbar2.value).style.display ="flex";
    }
    if(checkbar3.checked){
        document.getElementById(checkbar3.value).style.display ="flex";
    }
    if(checkbar4.checked){
        document.getElementById(checkbar4.value).style.display ="flex";
    }
}