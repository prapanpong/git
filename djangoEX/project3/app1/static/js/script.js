function changeText(){
    document.getElementById("demo").innerHTML = "This is Javascript test";
}

function changeData (strText,strColor,strSize){
    document.getElementById("myArea").innerHTML=strText;
    document.getElementById("myArea").style.backgroundColor=strColor;
    document.getElementById("myArea").style.fontSize=strSize;
    document.getElementById("myArea").style.border= "5px dotted pink";
    document.getElementById("myArea").style.width= "500px";
    document.getElementById("myArea").style.height= "500px";




}