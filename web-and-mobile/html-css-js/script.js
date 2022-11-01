window.addEventListener("load", function ()
{
    //get click element references
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");

    //counter value
    let counter = 0;

    //click button function
    let clickButtonFunction = function ()
    {
        //incrument counter
        counter++;

        //update counter value
        clickCounterElement.innerHTML = counter;
    };

    //attcah the button function
    clickButtonElement.addEventListener("click", clickButtonFunction);
});